# Sistema de Gestión de Citas Universitarias

## Descripción
Aplicación web para registrar usuarios y gestionar citas de atención universitaria. Desarrollado bajo arquitectura cliente-servidor con Flask y desplegado en la nube.

## Autor
- **Luis Linares** – Desarrollo individual (autorizado por la docente).

## Tecnologías
- **Backend:** Python 3.11, Flask, Flask-Login, SQLAlchemy.
- **Base de Datos:** SQLite.
- **Frontend:** HTML5, CSS3, Bootstrap 5.
- **DevOps:** GitHub Actions (CI), Docker, Render (CD).

## Estado del Proyecto: Versión Candidata (v1.0.0-rc1)
- [x] Registro de usuarios
- [x] Inicio de sesión seguro (Hashing)
- [x] Agendar citas (con validación de colisión)
- [x] Panel de administrador
- [x] Despliegue en Nube (Render)
- [x] Pipeline CI/CD automatizado
- [x] Gestión de incidencias y trazabilidad

## Instrucciones de Ejecución Local
1. Clonar el repositorio: `git clone https://github.com/LuisLinaresRojas/gestion-citas.git`
2. Crear un entorno virtual: `python -m venv venv`
3. Activar entorno: `venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Linux/Mac)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Ejecutar la app: `python app.py`

## Ejecución con Docker
1. Construir la imagen: `docker build -t gestion-citas .`
2. Correr el contenedor: `docker run -p 8000:8000 gestion-citas`

## Enlaces y Evidencias
- **Repositorio:** https://github.com/LuisLinaresRojas/gestion-citas
- **Entorno en Producción (Render):** https://gestion-citas-bxka.onrender.com
- **Tablero Kanban:** https://github.com/LuisLinaresRojas/gestion-citas/projects

## Credenciales de Prueba (Admin)
- **Correo:** admin@demo.com
- **Contraseña:** admin123

## Integración Continua (CI)
El proyecto cuenta con un pipeline en GitHub Actions (`.github/workflows/ci.yml`) que instala dependencias y ejecuta pruebas automatizadas con `pytest` en cada Push o Pull Request hacia las ramas `main` y `develop`.