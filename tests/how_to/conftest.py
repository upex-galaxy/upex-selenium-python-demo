import pytest
# * Primero, se importa siempre "pytest" librería de Python para realizar pruebas (the best!)
# * A continuación, verás que los imports de nuestros archivos deben comenzar siempre desde el root directory "tests"
from tests.drivers.chromedriver import *
# * Aquí se importa todos los artilugios generado de nuestro archivo de drivers!
# * En el archivo chromedriver en especial, se alojan todos  los TestUtils para nuestras pruebas.

# * Fixture para configurar y cerrar el navegador


@pytest.fixture
def setup():
    # * Crear nueva instancia del Driver y los Utils:
    web = chromeDriver()
    element = Locators(web)
    # * ESTA ES UNA FORMA INTELIGENTE DE MANEJAR TUS PRUEBAS! la forma más prolija que te puedo enseñar!

    # * Se obtiene la URL de Google y se verifica el título
    web.implicitly_wait(10)
    element.goto("https://google.com")
    # *  Se verifica el título de la página
    title = web.title
    assert title == "Google"

    # * Fin de la Precondición.
    # Aquí puedes colocar el código que quieres retornar del setup.
    yield web, element
    # * Código de la PostCondición.
    # web.quit() # *Se cierra el navegador


if __name__ == "__main__":
    # * Ejecución de las pruebas utilizando pytest
    pytest.main()
