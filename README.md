#  Proyecto Urban Grocers

## Descripción del Proyecto
Se implementan pruebas automatizadas para la API de **Urban Grocers**, verificando la funcionalidad del endpoint de creación de kits.  
Las pruebas aseguran que el sistema maneje correctamente la validación de datos, autenticación y restricciones de entrada.  

## Fuente de Documentación
Las pruebas se basan en la documentación de la API proporcionada por **Urban Grocers**, utilizando **apiDoc** como referencia para entender los endpoints y sus parámetros.  
Para más detalles, consulta:  
 `<the url of the launched server>/docs/>`  

## Tecnologías y Técnicas Utilizadas  

- **Python** : Lenguaje de programación para automatización.  
- **Pytest** : Framework para escribir y ejecutar pruebas.  
- **Requests** : Librería para interactuar con la API.  
- **Git y GitHub** : Control de versiones y almacenamiento del código.  
- **Metodología TDD** : Desarrollo basado en pruebas automatizadas.  

## Reglas y Pasos para Ejecutar las Pruebas

###  **Clonar el Repositorio**
```sh
git clone <git@github.com:Victoriamdz/qa-project-Urban-Grocers-app-es.git>
cd <qa-project-Urban-Grocers-app-es>

###  **Instalar dependencias**

pip install -r requirements.txt


###  **Ejecutar pruebas**
pytest create_kit_name_kit_test.py




