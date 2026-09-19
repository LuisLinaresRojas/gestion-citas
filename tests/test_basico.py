def test_suma_basica():
    """Prueba trivial para verificar que pytest funciona."""
    assert 1 + 1 == 2

def test_importacion_app():
    """Verifica que la aplicación Flask se pueda importar."""
    from app import app
    assert app is not None