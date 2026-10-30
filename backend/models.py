from datetime import UTC, datetime
from decimal import Decimal
from enum import Enum

from sqlalchemy import DateTime
from sqlmodel import Field, SQLModel


def ahora() -> datetime:
    return datetime.now(UTC)


class Motivo(str, Enum):
    todo_tipo = "todo_tipo"
    solo_vpo = "solo_vpo"
    asesoramiento = "asesoramiento"
    vender = "vender"


class RolEmpleado(str, Enum):
    admin = "admin"
    marketing = "marketing"
    comercial = "comercial"


class EstadoOportunidad(str, Enum):
    nuevo = "nuevo"
    contactado = "contactado"
    visita = "visita"
    reserva = "reserva"
    comprador = "comprador"
    descartado = "descartado"


class TipoEvento(str, Enum):
    visita = "visita"
    clic_cta = "clic_cta"
    formulario_enviado = "formulario_enviado"


class Empleado(SQLModel, table=True):
    __tablename__ = "empleados"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    email: str = Field(unique=True, index=True)
    rol: str
    especialidad: str | None = None
    activo: bool = True


class Cliente(SQLModel, table=True):
    __tablename__ = "clientes"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    email: str = Field(unique=True, index=True)
    telefono: str | None = None
    origen: str | None = None
    creado_en: datetime = Field(default_factory=ahora, sa_type=DateTime(timezone=True))


class Promocion(SQLModel, table=True):
    __tablename__ = "promociones"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str | None = None
    zona: str
    es_vpo: bool = False
    precio_desde: Decimal = Field(max_digits=10, decimal_places=2)
    num_viviendas: int | None = None


class Oportunidad(SQLModel, table=True):
    __tablename__ = "oportunidades"

    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="clientes.id", index=True)
    promocion_id: int | None = Field(default=None, foreign_key="promociones.id", index=True)
    empleado_id: int | None = Field(default=None, foreign_key="empleados.id", index=True)
    motivo: str = Field(index=True)
    estado: str = Field(default=EstadoOportunidad.nuevo.value, index=True)
    mensaje: str | None = None
    creado_en: datetime = Field(default_factory=ahora, sa_type=DateTime(timezone=True))


class Evento(SQLModel, table=True):
    __tablename__ = "eventos"

    id: int | None = Field(default=None, primary_key=True)
    session_id: str = Field(index=True)
    promocion_id: int | None = Field(default=None, foreign_key="promociones.id", index=True)
    cliente_id: int | None = Field(default=None, foreign_key="clientes.id", index=True)
    tipo: str = Field(index=True)
    creado_en: datetime = Field(default_factory=ahora, sa_type=DateTime(timezone=True))