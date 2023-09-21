import pytest
# * Esta importación es clave para dar type al setup del fixture:
from tests.types import test
# * También puedes importar lo que necesites de los módulos y dependencias:
from selenium.webdriver.common.keys import Keys

# #* A continuación, verás la Class en Python, representa al famoso Test Suite (conocido  como el "TS"),
# # Aquí debes colocar el nombre del TS (el nombre de la Feature de la Historia de Usuario básicamente)
# # Recuerda escribir el nombre de esta Clase en convention camelCase como se acostumbra:


class TestSuiteExample:
    # * A continuación, verás la Función en Python, representa al Caso de Prueba (TC como sabrás)
    # Aquí debes utilizar SIEMPRE el prefijo "test_" al principio del nombre de la nomenclatura,
    # En esta caso como TC, tienes que escribir el nombre de la función en convention snake_case:
    def test_example(self, setup):
        web, element = setup
    # * El parámetro "self" identifica que este TC está dentro del TS (esta Class), es un deber colocarlo.
    # * El parámetro "setup" es una función del Fixture en "conftest.py", se usa para muchas cosas!
    # * En este caso importante, el "setup" proviene dentro del archivo "conftest.py" del mismo directorio.
    # * Cuando se usa como parámetro dentro de una función test, se ejecuta primero la función fixture (precondición background) antes del TC mismo.
    # * Es como haber usado un BeforeEach. También incluye el AfterEach.
    # * Lo cual lo hace un SUPER PODER para las pruebas parametrizadas. También hace que el test se vea limpio!

        # * A continuación: Cómo se escriben los scripts de Selenium para hacer E2E Testing:
        # todo WHEN: User inserts "Selenium" in the Search Box
        # El método getName realmente proviene de un TestUtil que se importó desde un archivo de drivers.
        # El método .send_keys() se usa para escribir en inputs.
        searchBar = element.getName("q")
        searchBar.send_keys("Selenium")

        # todo AND: User press ENTER
        searchBar.send_keys(Keys.RETURN)

        url = web.current_url
        assert "/search" in url  # URL contains the string

        # todo ---- para aprender más sobre comandos, investiga en la Documentación! ;)


# * Dato interesante! SIEMPRE agregar este siguiente bloque de código del if en cada prueba.
# Si quieres entender más a fondo qué hace exactamente este bloque, pregúntale a ChatGPT XD
# En términos simples, es una condición que dice que si este archivo se llama únicamente directamente, se ejecutará la prueba de pytest, así Python no ejecutará este archivo sin nuestro aviso de ejecución.
if __name__ == "__main__":
    pytest.main()
