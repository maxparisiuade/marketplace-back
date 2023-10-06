# FastAPI

Este es un proyecto de una aplicación web construida con FastAPI y administrada con Poetry.

## Instalación

Asegúrate de tener Poetry instalado. Si no lo tienes, puedes instalarlo siguiendo las [instrucciones aquí](https://python-poetry.org/docs/#installation).

## Comandos para su ejecución

Installar las dependencias del proyecto

```bash
poetry install
```

Actualizar las dependencias del proyecto si es necesario

```bash
poetry update
```

Inicializar el entorno virtual

```bash
poetry shell
```

Ejecutar la app

```bash
python -m main
python -m uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```
