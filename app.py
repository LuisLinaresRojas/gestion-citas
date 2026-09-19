from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, Usuario, Cita
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-proyecto'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///citas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        password = request.form['password']
        
        if Usuario.query.filter_by(correo=correo).first():
            flash('El correo ya está registrado')
            return redirect(url_for('registro'))
        
        nuevo = Usuario(
            nombre=nombre,
            correo=correo,
            password=generate_password_hash(password)
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect(url_for('login'))
        
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        user = Usuario.query.filter_by(correo=correo).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Credenciales incorrectas')
        
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/agendar', methods=['GET', 'POST'])
@login_required
def agendar():
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora = request.form['hora']
        motivo = request.form['motivo']
        
        # Validar que no exista una cita en la misma fecha y hora
        existe = Cita.query.filter_by(fecha=fecha, hora=hora).first()
        if existe:
            flash('Ese horario ya está ocupado')
            return redirect(url_for('agendar'))
            
        nueva = Cita(fecha=fecha, hora=hora, motivo=motivo, usuario_id=current_user.id)
        db.session.add(nueva)
        db.session.commit()
        flash('Cita agendada exitosamente')
        return redirect(url_for('mis_citas'))
        
    return render_template('agendar.html')

@app.route('/mis-citas')
@login_required
def mis_citas():
    citas = Cita.query.filter_by(usuario_id=current_user.id).all()
    return render_template('agendar.html', citas=citas)
@app.route('/admin')
@login_required
def admin():
    if current_user.rol != 'admin':
        flash('Acceso denegado. Solo administradores.')
        return redirect(url_for('index'))
    citas = Cita.query.all()
    return render_template('admin.html', citas=citas)

@app.route('/admin/confirmar/<int:id>')
@login_required
def confirmar(id):
    if current_user.rol != 'admin':
        return redirect(url_for('index'))
    c = Cita.query.get_or_404(id)
    c.estado = 'confirmada'
    db.session.commit()
    flash('Cita confirmada')
    return redirect(url_for('admin'))

@app.route('/admin/cancelar/<int:id>')
@login_required
def cancelar(id):
    if current_user.rol != 'admin':
        return redirect(url_for('index'))
    c = Cita.query.get_or_404(id)
    c.estado = 'cancelada'
    db.session.commit()
    flash('Cita cancelada')
    return redirect(url_for('admin'))

# Crea las tablas al iniciar (necesario para Gunicorn/Docker)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)