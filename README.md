# S.W.A.: Snippets with attitude!

## Proyecto SWA (snippets with attitude)

### Requerimientos (Linux)
- Librerias dev de MySQL
- Librerias de desarrollo de python
- Herramientas de desarrollo (gcc, otros)

### Creando ambiente de desarrollo

Usando virtual env:
virtualenv ENV/
source ENV/bin/activate
pip install -r requirements.txt

### Compilación de SASS

En web/static/
`sass --sourcemap=none --watch scss/:css/ --style compressed`

### Corriendo el servidor de desarrollo

En swa/swa/
`python manage.py runserver`
