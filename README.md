# Pre-entrega Proyecto Final - Automatización de Testing - José María Damonte

Repositorio para proyecto del curso de Automatización QA de Talento Tech 2025.
Se implementan pruebas automatizadas para el sitio SauceDemo, mediante la utilización de Selenium WebDriver y Python.

## Propósito del Proyecto

El objetivo para la pre-entrega es automatizar los flujos de uso del sitio web, para representar las interacciones de un usuario:

- Login con credenciales válidas e inválidas
- Verificación del catálogo de productos
- Interacción con el carrito de compras (añadir productos y verificar su contenido)
- Cierre de sesión

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Pytest**: Framework de testing para realizar las pruebas y validaciones.
- **Selenium**: Para la automatización de las interacciones con la interfaz web, empleando Chrome WebDriver.
- **Git/GitHub**: Para control de versiones y compartir el código en un repositorio.

## Instalación de Dependencias

1. Asegurarse de tener Python 3.7 o superior instalado.
2. Crear un entorno virtual (python venv y el nombre del entorno, en este caso "env"): `py -m venv env`
3. Activar el entorno virtual: `.\env\Scripts\activate`
3. Instala las dependencias necesarias desde el archivo "requirements.txt":

Estando en la raiz del proyecto, `py -m pip install -r requirements.txt`

## Ejecución de Pruebas

Desde la raiz del proyecto: `py run_tests.py`

## Autor
José María Damonte