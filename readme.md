<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![vscode-logo]][vscode-site] [![selenium-logo]][selenium-site] [![python-logo]][python-site] [![behave-logo]][behave-site]

<h1 align="center">🧪Testing Automation: 🐍Selenium 4.5 +Behave</h1>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="https://user-images.githubusercontent.com/91127281/200486232-5697197c-0541-4496-a487-bc720f234a1b.png" alt="Logo" width="" height="270">
  </a>

<h2 align="center">🧪SELENIUM-PYTHON🧪</h2>

  <p align="center">
    Selenium + Pytest + Behave (Gherkin) in VSCode
    <br />
    <a href="https://github.com/upex-galaxy/selenium-python"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/upex-galaxy/selenium-python/blob/selpex/Tests/start/upexTest.py">View Demo</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->

# Pruebas Automatizadas con Python🐍

¡Python es un lenguaje de programación que no necesita presentación! Es uno de los lenguajes preferidos cuando se trata de proyectos que involucran aprendizaje automático (ML) , inteligencia artificial (IA) y más. En un campo de batalla diferente, la combinación de Selenium Python es ampliamente preferida en lo que respecta a la automatización de sitios web.

Según la Encuesta de desarrolladores de Stack Overflow 2021, Python es el tercer lenguaje más popular después de JavaScript y HTML/CSS. La destreza de Selenium y Python ayuda a automatizar las interacciones con WebElements en el DOM (Document Object Model).

# CÓMO EMPEZAR DIRECTO AL GRANO:

1. **Precondición**:

   - Tener instalado Anaconda en la PC local (Es un Manager de Ambiente Virtual).
   - Puedes confirmar abriendo "Anaconda Prompt" y ejecutar `conda --version`
   - Setear la Variable de Ambiente en Windows con el mismo path de anaconda, normalmente sería: `C:\Users\Username\anaconda3` para poder usar Anaconda en las terminales.

2. **Clona el Proyecto con la Terminal de VSC**:

   ```
   git clone https://github.com/upex-galaxy/L1-selpy-demo.git
   ```

3. `Opción VSCODE:` **Abrir el Command Palette (Ctrl+Shift+P) y realizar las acciones:**

   - Seleccionar Python: Create Environment
   - Seleccionar Conda
   - Seleccionar versión de Python (la que recomiende)
   - Esperar que realice el proceso de creación de environment.
   - Debería crearse un archivo `.conda` en el root del repo.
   - Para ver el listado en envs creados con `conda info --envs`
   - Copia el env creado full path.
   - Activar el environment con `conda activate <full_path_env>`

4. `Opción Manual (Cómoda):` **Entra en la Carpeta del Proyecto clonado `selenium-python` en VSC y Crea un Ambiente de Conda con la Terminal**:

   ```
   conda create -n <env_name>
   ```

   - **EN WINDOWS: Activa el Ambiente Conda creado a través de**:

   ```
   source activate <env_name>
   ```

   - **EN LINUX: Activa el Ambiente Conda creado a través de**:

   ```
   activate <env_name>
   ```

5. **MUY IMPORTANTE: ACTIVAR EL INTÉRPRETE PYTHON** Por más que se hayan instalado las dependencias, es importante activar ahora el intérprete para poder trabajar sobre el mismo. Para ello:

   - Abrir el Command Palette (Ctrl+Shift+P)
   - Seleccionar la opción: "Python: select interpreter"
   - Seleccionar la ruta python que el ENV activado para el proyecto.
   - Refrescar VSCODE para efectuar todas las configuraciones.

6. **Instala todas las dependencias del archivo requirements.txt con el ENV creado de Conda, ejecutando el siguiente comando luego haber activado el ambiente conda y el intérprete de Python**:
   ```
   pip install -r requirements.txt
   ```
   - Aquí se está usando con el mismo pip se instala las dependencias del proyecto actual ubicado. Esto instalará todas las dependencias del Proyecto en el ENV creado para comenzar a trabajar directo.
   - Si estás usando la Opción VSCODE, el cual usa una ruta directa, debes usar esta misma ruta y adentrarte en el archivo python.exe para ejecutar el mismo comando.

# PLAN DE PRUEBA: ESTRATEGIA Y DISEÑO

### 🚩NORMATIVAS A SEGUIR:

1. Perfecta Nomenclatura del nombre de Archivo de prueba: <br> `test_{GXID}_{StoryShortName}.py ej: test_GX50_AgregarItemsAlCart.py`
2. El Archivo de Prueba dentro estar en el directorio "coverage" con la carpeta del Componente correspondiente, ejemplo: <br> `tests/coverage/example/test_example.py`.
3. Buen diseño del Test Suite elaborado (Esto implica que se vean bien el código en general, que al menos funcione).
4. **En caso de usar el Utils u otros módulos**: Ya los tienes todo disponible en el archivo principal Testbase que puedes importar desde tu archivo, usando: <br> `from tests.testbase import *`.
5. **En caso de usar PageObjectModel**: Aplicar las buenas prácticas del patrón de diseño POM. Recuerda usar el tipo de función lambda para generar los locators y crear buenos nombres de los métodos.
6. **En caso de usar el CI Pipeline**: Usar únicamente el archivo predeterminado del proyecto `sanity.yml`, y asegurarse de modificarlo correctamente (Solo cambiar el Path del Test Suite) y no borrar o cambiar nada más, que funcione y pase los Checks. El archivo `regression.yml` se ejecutará automaticamente cuando los cambios hayan mergeado a QA.
7. **En caso de usar Behave (BDD)**: Chequear que el archivo Gherkin (.feature) y los StepDefinitions (.py) estén correctamente diseñados. Lee las guías o el curso para más información de su uso.

---

# 🚩NIVELES DE TESTER QA en UPEX Galaxy:

El programa **UPEX Galaxy** está diseñado para guiar a los Testers a través de 2 Etapas (Career Paths). Cada Etapa conlleva ciertos **NIVELES** que el Tester debe alcanzar para llegar a su mayor **SENIORITY**:

## QA Engineer (Pruebas Manuales)

Capacidad de realizar análisis, planificación, ejecución y gestión de:

- Pruebas Manuales de UI
- Bases de Datos
- API Testing

### 🧪L1

Capaz de realizar tareas (US) sencillas de frontend sin mucha complejidad.

##### Prácticas:

- Entiende y puede seguir guías y protocolos de prueba previamente definidos.
- Identifica errores obvios en la interfaz y reporta con claridad.
- Familiarizado con herramientas básicas de testing y reporting.
- Capaz de realizar pruebas de regresión siguiendo casos de prueba definidos.

### 🧪L2

Capaz de realizar tareas (US) avanzadas de frontend y también tareas de Backend (Pruebas de Bases de Datos y Pruebas de API).

##### Prácticas:

- Realiza pruebas exploratorias identificando puntos críticos en las aplicaciones.
- Puede diseñar casos de prueba simples basados en requisitos.
- Familiarizado con SQL básico para realizar pruebas en Bases de Datos.
- Inicia pruebas básicas en APIs usando herramientas como Postman o similares.
- Entiende la importancia de ciclos de vida de defectos y los gestiona correctamente.

### 🧪L3

Capaz de realizar tareas (US) de performance y/o diseñar nuevas Historias de Usuario.

##### Prácticas:

- Diseña y ajusta casos de prueba complejos basados en cambios de requisitos.
- Identifica y reporta problemas de rendimiento usando herramientas básicas.
- Realiza pruebas exploratorias avanzadas e identifica áreas no cubiertas.
- Gestiona los Planes de Prueba (Cobertura, Regresión, Sanity, Smoke) de manera efectiva.
- Ofrece guía y mentoría a testers de niveles inferiores (Capacidad de ser Tutor).
- Tiene una comprensión básica sobre automatización de pruebas.

## QA Automation Engineer (Pruebas Automatizadas)

Capacidad de realizar análisis, planificación, ejecución y gestión de:

- Pruebas Automatizadas de E2E
- Integration Testing (Aplicando para cualquiera de los Frameworks de automatización de Browsers/Apps)

### 🧪L3

Capaz de realizar tareas (TechDept) para Automatizar pruebas UI de historias implementadas.

##### Prácticas:

- Capaz de manejar el flujo completo de trabajo ordinario.
- Capaz de realizar pruebas Frontend con data sin iteración (hardcodeada).
- Capaz de realizar Page-Object-Model básico.
- Capaz de realizar controles de versionado de código (conocimiento básico en GIT).

### 🧪L4

Capaz de realizar tareas (TD) para Automatizar pruebas complejas y de integración de historias implementadas.

##### Prácticas:

- Capacidad de resolución de problemas y conflictos de pruebas (Debugging).
- Capaz de realizar pruebas E2E con data en iteración (Parametrizadas).
- Capaz de escribir código con Excelentes prácticas y principios (POM, “DRY”, etc.).
- Capaz de escribir scripts de prueba con Estructura de Datos, condicionales, bucles, etc.
- Capaz de entender y ejecutar Pipelines de Regresión en Continuous Integration (CI).
- Capaz de escribir scripts de prueba para intercepción y assertions de API Testing.

### 🧪L5

Capaz de realizar cualquier tarea (TD) de Automatización y gestionar los Planes de Prueba.

##### Prácticas:

- Capacidad de resolución de conflictos de GIT con facilidad.
- Capacidad de resolución de problemas de ambientes y errores de config del Repo.
- Capaz de realizar Planes de Prueba generales y para Automatización de pruebas.
- Capaz de planificar, armar y hacer funcionar los Repositorios de Automatización de Prueba.
- Capaz de configurar integraciones de aplicaciones de Reporte de Prueba con el Repo.
- Capaz de realizar pruebas automatizadas de Performance (con ciertas herramientas).

---

### 🧙🏻‍♂️APRENDE Y GANA EXPERIENCIA COMO QA AUTOMATION EN UPEX GALAXY🚀

Suscríbete a un Sprint y trabaja como un QA Automation Engineer!

### 🚩ENTRA EN [UPEXDOCU](https://linktree.com/upexjira) Y BUSCA LAS GUÍAS DE SELENIUM-PYTHON AL GRANO!

---

## CURSO YOUTUBE DE SELENIUM-PYTHON AL GRANO:

- [🛸CURSO: "AUTOMATION SELENIUM-PYTHON AL GRANO" (UPEX GALAXY)]()

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[vscode-logo]: https://img.shields.io/badge/VSCode-black?logo=visualstudiocode&style=for-the-badge
[vscode-site]: https://code.visualstudio.com/
[selenium-logo]: https://img.shields.io/badge/Selenium-black?logo=selenium&style=for-the-badge
[selenium-site]: https://www.selenium.dev/documentation/webdriver/
[python-logo]: https://img.shields.io/badge/Python-black?logo=python&style=for-the-badge
[python-site]: https://www.python.org/
[behave-logo]: https://img.shields.io/badge/Behave-black?logo=cucumber&style=for-the-badge
[behave-site]: https://behave.readthedocs.io/
[slack-logo]: https://img.shields.io/badge/Slack-black?logo=slack&style=for-the-badge
[slack-join]: https://linktr.ee/upex
[linkedin-logo]: https://img.shields.io/badge/LinkedIn-black?style=for-the-badge&logo=linkedin
[linkedin-link]: https://www.linkedin.com/in/elyermad/
