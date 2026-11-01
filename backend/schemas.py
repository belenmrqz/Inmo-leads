from decimal import Decimal

from sqlmodel import SQLModel


class PromocionRead(SQLModel): # Define qué campos devuelve la API
    id: int
    nombre: str
    descripcion: str | None
    zona: str
    es_vpo: bool
    precio_desde: Decimal
    num_viviendas: int | None
    