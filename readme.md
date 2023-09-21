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

<h2 align="center">🧪SELPEX🧪</h2>

  <p align="center">
    Selenium + Python + Behave (Gherkin) in VSCode
    <br />
    <a href="https://github.com/upex-galaxy/selenium-python"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/upex-galaxy/selenium-python/blob/selpex/Tests/start/upexTest.py">View Demo</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->

# Pruebas Automatizadas con Python🐍

¡Python es un lenguaje de programación que no necesita presentación! Es uno de los lenguajes preferidos cuando se trata de proyectos que involucran aprendizaje automático (ML) , inteligencia artificial (IA) y más.En un campo de batalla diferente, la combinación de Selenium Python es ampliamente preferida en lo que respecta a la automatización de sitios web.

Según la Encuesta de desarrolladores de Stack Overflow 2021, Python es el tercer lenguaje más popular después de JavaScript y HTML/CSS. La destreza de Selenium y Python ayuda a automatizar las interacciones con WebElements en el DOM (Document Object Model).

# TUTORIAL COMPLETO PASO A PASO CREACIÓN DE PROYECTO (Instalación con Anaconda🐍 + Diseño y Ejecución de Pruebas)

[CURSO: "Selenium AL GRANO" (Python+BDD)](https://upexgalaxy6.atlassian.net/wiki/spaces/UG/pages/917969)

- Precondiciones del Proceso
- GETTING STARTED
- CONFIGURACIÓN Y ESTRUCTURA del Working Tree
- HACER EL PRIMER SCRIPT DE PRUEBA DE SELENIUM
- Precondiciones para escribir los Test Suites
- NOMENCLATURA DEL ARCHIVO DE PRUEBA para usar Pytest
- IMPORTAR las dependencias: Selenium + WebDriver
- ESTRUCTURA DE SCRIPT DE PRUEBA (TEST SUITE)
- SCRIPT DE PRUEBA
- GUÍA PARA USAR LOS WEB ELEMENTS
- CORRER EL SCRIPT DE PRUEBA EN VSCODE
- Cómo Configurar el Test Runner para el proyecto Selenium-Python

# CÓMO EMPEZAR DIRECTO AL GRANO:

1. **Precondición**:

   - Tener instalado Anaconda en la PC local (Es un Manager de Ambiente Virtual).
   - Puedes confirmar abriendo "Anaconda Prompt" y ejecutar `conda --version`
   - Setear la Variable de Ambiente en Windows con el mismo path de anaconda, normalmente sería: `C:\Users\Username\anaconda3` para poder usar Anaconda en las terminales.

2. **Clona el Proyecto con la Terminal de VSC**:

   ```
   git clone https://github.com/upex-galaxy/selenium-python.git
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

6. **Instala todas las dependencias del archivo requirements.txt en el ENV creado de Conda (el equivalente a package.json en Node.js), ejecutando este comando en especial con la ruta de los envs de Conda para usar el intérprete de python del env creado**:
   ```
   C:/Users/<Usuario>/anaconda3/envs/<env_name>/python.exe -m pip install -r requirements.txt
   ```
   - Aquí se está usando el env creado para llegar a su intérprete python que con el mismo pip se instala las dependencias del proyecto actual ubicado. Esto instalará todas las dependencias del Proyecto en el ENV creado para comenzar a trabajar directo.
   - Si estás usando la Opción VSCODE, el cual usa una ruta directa, debes usar esta misma ruta y adentrarte en el archivo python.exe para ejecutar el mismo comando.

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
