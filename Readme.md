####################################################################################
# SISTEMA EXPERTO PARA EL MANEJO INTEGRADO DEL GORGOJO DE LOS ANDES #
####################################################################################

## Importante:
    - Decir que se requiere Python desde 3.5 a la 3.8
    debido a que la libreria experta solo acepta esas versiones
## Si tiene una version superior lo recomendable es implementar Pypi puede seguir el siguiente tutorial:

- https://pypi.org/project/pypi-install/

## instalaciones que necesitas Django y la libreria Experta

### Primera opción:
            - pip install -r requeriments.txt

### Segunda Opción:
            - pip install Django
            - pip install experta==1.9.4

## Test
#### Para ejecutar los test necesitas:
##### Windows
            - py manage.py test questionsRules

##### Linux / Mac
            -python3 manage.py test questionsRules/
## Para ejecutar el programa

### Asegurate de estar dentro de la carpeta SEMIG
### Una ves dentro de la carpeta ejecuta:

#### Linux / Mac
            - python3 manage.py runserver

#### Windows
            - py manage.py runserver

