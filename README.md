# Recuperatorio - Estaciones del SMN
## alumno
Leo Chambilla

## Descripción

Este proyecto consiste en un programa de Python que permite leer observaciones meteorológicas del Servicio Meteorológico Nacional (SMN) desde un archivo JSON.

Cada observación se representa mediante un objeto de la clase `Observacion_Clase`.

El programa permite:
- Cargar las observaciones del archivo JSON.
- Validar los datos de cada observación.
- Ignorar los registros que contienen datos inválidos.
- Filtrar las observaciones por estación meteorológica.
- Calcular la cantidad de observaciones, la temperatura mínima, la máxima y el promedio.

## Archivos del proyecto

- `observacion.py`: contiene la clase `Observacion_Clase`, sus atributos, validaciones y métodos.
- `consultar_clima.py`: contiene las funciones para cargar, filtrar y resumir las observaciones.
- `main.py`: permite ejecutar el programa desde la terminal.
- `observaciones.json`: contiene los datos meteorológicos.
- `test_observacion.py`: contiene las pruebas de la clase `Observacion_Clase`.
- `requirements.txt`: contiene las dependencias necesarias.

## Requisitos

- Python 3.
- pytest.

## Instalación

Instalar las dependencias con:

```bash
python -m pip install -r requirements.txt
```

## Ejecución

Desde la terminal, ejecutar:

```bash
python main.py observaciones.json "AEROPARQUE AERO"
```

Se debe indicar primero la ruta del archivo JSON y después el nombre de la estación que se desea consultar.

## Ejecución de las pruebas

Para ejecutar las pruebas:

```bash
python -m pytest -v
```


