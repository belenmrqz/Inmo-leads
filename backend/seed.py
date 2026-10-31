from decimal import Decimal

from sqlmodel import Session, select

from database import engine
from models import Empleado, Promocion, RolEmpleado

PROMOCIONES = [
    {
        "nombre": "Residencial Los Olivos",
        "descripcion": "Viviendas de protección oficial con zonas verdes y garaje.",
        "zona": "Tomares",
        "es_vpo": True,
        "precio_desde": Decimal("135000.00"),
        "num_viviendas": 48,
    },
    {
        "nombre": "Torre Aljarafe",
        "descripcion": "Pisos de obra nueva con terraza y vistas despejadas.",
        "zona": "Mairena del Aljarafe",
        "es_vpo": False,
        "precio_desde": Decimal("210000.00"),
        "num_viviendas": 32,
    },
    {
        "nombre": "Jardines del Guadalquivir",
        "descripcion": "Vivienda protegida cerca del río, con piscina comunitaria.",
        "zona": "Sevilla Este",
        "es_vpo": True,
        "precio_desde": Decimal("128500.00"),
        "num_viviendas": 60,
    },
    {
        "nombre": "Mirador de Bormujos",
        "descripcion": "Promoción de pisos y áticos de alta eficiencia energética.",
        "zona": "Bormujos",
        "es_vpo": False,
        "precio_desde": Decimal("245000.00"),
        "num_viviendas": 24,
    },
]

EMPLEADOS = [
    {"nombre": "Carlos Ruiz", "email": "carlos@inmo.test",
     "rol": RolEmpleado.comercial.value, "especialidad": "todo_tipo"},
    {"nombre": "Lucía Pérez", "email": "lucia@inmo.test",
     "rol": RolEmpleado.comercial.value, "especialidad": "solo_vpo"},
    {"nombre": "Marta León", "email": "marta@inmo.test",
     "rol": RolEmpleado.comercial.value, "especialidad": "asesoramiento"},
    {"nombre": "Javier Sanz", "email": "javier@inmo.test",
     "rol": RolEmpleado.comercial.value, "especialidad": "vender"},
    {"nombre": "Ana Torres", "email": "ana@inmo.test",
     "rol": RolEmpleado.marketing.value, "especialidad": None},
]


def poblar() -> None:
    with Session(engine) as session:
        if session.exec(select(Promocion)).first() is None:
            session.add_all(Promocion(**datos) for datos in PROMOCIONES)
        if session.exec(select(Empleado)).first() is None:
            session.add_all(Empleado(**datos) for datos in EMPLEADOS)
        session.commit()
    print("Datos de prueba cargados")


if __name__ == "__main__":
    poblar()