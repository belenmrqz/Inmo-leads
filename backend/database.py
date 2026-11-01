from sqlmodel import Session, create_engine

from config import settings

# ABRE LA CONEXIÓN CON POSTGRESQL Y REPARTE SESIONES AL RESTO DEL CÓDIGO
# Un único motor para toda la app, sabe dónde está PostgreSQL y reutiliza
# conexiones. No se conecta hasta que se hace la primera consulta.

engine = create_engine(settings.database_url)


def get_session():
    """Entrega una sesión por petición y la cierra al terminar."""
    with Session(engine) as session:
        # yield (y no return) para que FastAPI pueda cerrar la sesión después
        yield session