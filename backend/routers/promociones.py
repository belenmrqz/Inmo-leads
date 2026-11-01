from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from database import get_session
from models import Promocion
from schemas import PromocionRead

# Aquí es donde viven los endpoints, y el archivo que más conviene dominar.

# Todas las rutas de este archivo empiezan por /promociones
router = APIRouter(prefix="/promociones", tags=["promociones"])

# FastAPI inyecta una sesión de base de datos nueva en cada petición
SessionDep = Annotated[Session, Depends(get_session)]


@router.get("", response_model=list[PromocionRead])
def listar_promociones(session: SessionDep, es_vpo: bool | None = None):
    """Lista las promociones. Con ?es_vpo=true|false filtra por tipo."""
    # La consulta se construye por partes y se ejecuta al final con exec()
    consulta = select(Promocion)
    # Se compara con None (no con False) porque es_vpo=false también es un filtro
    if es_vpo is not None:
        consulta = consulta.where(Promocion.es_vpo == es_vpo)
    return session.exec(consulta.order_by(Promocion.id)).all()


@router.get("/{promocion_id}", response_model=PromocionRead)
def obtener_promocion(promocion_id: int, session: SessionDep):
    promocion = session.get(Promocion, promocion_id)
    if promocion is None:
        raise HTTPException(status_code=404, detail="Promoción no encontrada")
    return promocion