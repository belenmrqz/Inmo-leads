from decimal import Decimal

from sqlmodel import SQLModel


class PromocionRead(SQLModel):
    id: int
    nombre: str
    descripcion: str | None
    zona: str
    es_vpo: bool
    precio_desde: Decimal
    num_viviendas: int | None
    