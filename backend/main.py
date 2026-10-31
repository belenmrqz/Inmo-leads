from fastapi import FastAPI

from routers import promociones

app = FastAPI(title="Inmo Leads API")

app.include_router(promociones.router)


@app.get("/health")
def health():
    return {"status": "ok"}