from fastapi import FastAPI

app = FastAPI(title="Inmo Leads API")


@app.get("/health")
def health():
    return {"status": "ok"}