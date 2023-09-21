# Archivo de definiciones de pasos de prueba (StepDefinition) para behave

# Se importa todo el módulo behave
from behave import *

# Se importa el WebDriver necesario desde una ubicación específica en el directorio
# El uso de los puntos suspensivos (...) indica saltos hacia atrás en la estructura del directorio.
from tests.utils.drivers import *

# Definición de pasos de prueba utilizando decoradores


@given('we have behave installed')
def step_implA(context):
    # Implementación del paso dado (given), el parámetro context es necesario.
    pass


@when('we implement a test')
def step_implB(context):
    # Implementación del paso cuando (when)
    assert True is not False


@then('behave will test it for us!')
def step_implC(context):
    # Implementación del paso entonces (then)
    assert context.failed is False
