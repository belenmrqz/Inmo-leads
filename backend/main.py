from fastapi import FastAPI

from routers import promociones

# PUNTO DE PARTIDA DE LA API

app = FastAPI(title="Inmo Leads API") # Crea la app

app.include_router(promociones.router) # Engancha a la aplicación todas las rutas del router


@app.get("/health")
def health(): # Comprueba que la API está viva (la usará también el despliegue)
    return {"status": "ok"}
# Cuando ejecuto uv run fastapi dev main.py, FastAPI busca dentro del 
# archivo una variable con ese nombre