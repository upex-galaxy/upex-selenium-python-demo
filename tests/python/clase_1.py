# Esto es un Comentario.

# * Tipos de Datos Basicos:
a = 1212  # Int
b = 1212.2323  # Float
c = "Hola que onda"  # String
d = True  # Boolean
e = False  # Boolean
f = ["A", 5, True]  # Array/ list
g = (["A", 5, True], ["A", 5, True])  # Tuple
w = set({"A", 5, True})  # Sets
x = {"key": "123"}  # Objetos/Diccionarios


def aprender(framework: str):
    if not isinstance(framework, str):
        return 'NO SRING!'
    else:
        if (framework == 'selenium'):
            return 'Te recomiendo aprender Selenium-Python'
        if (framework == 'cypress'):
            return 'Te recomiendo aprender JavaScript con Promesas'
        if (framework == 'playwright'):
            return 'No hay nada mejor que un TypeScript y un Café'
        return 'No reconozco este framework'


# print(aprender(True))

ejemplo = ["pass", "pass", "fail", "pass", "fail",
           "pass", "pass", "fail", "pass", "fail"]


def get_all_tests_results(results: list):
    item = 1
    while item < len(results):
        for test in results:
            print("TC" + str(item) + ": " + test)
            item += 1


get_all_tests_results(ejemplo)
