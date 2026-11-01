from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel

import models  # noqa: F401
from config import settings

# AQUÍ SE CONECTA ALEMBIC CON EL PROYECTO
# Cada vez que ejecutas un comando de Alembic (revision, upgrade, current...), lo primero que se ejecuta es este archivo. Le responde a Alembic a dos preguntas:
# ¿Dónde está la base de datos?
# ¿Cómo se supone que debe ser? (tus modelos)

# Este es el objeto «Alembic Config», que permite acceder a los valores 
# del archivo .ini que se está utilizando.
config = context.config # El objeto que representa tu archivo alembic.ini

# Usa la base de datos de mi .env en lugar de la dirección de alembic.ini
config.set_main_option("sqlalchemy.url", settings.database_url)

# Interpreta el archivo de configuración para el registro de Python.
# Esta línea configura, básicamente, los registradores.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Añade aquí el objeto MetaData de tu modelo
# para que sea compatible con la «generación automática»
# from myapp import mymodel
# target_metadata = mymodel.Base.metadataa
target_metadata = SQLModel.metadata

# Se pueden obtener otros valores del archivo de configuración, definidos según las necesidades de env.py,
# de la siguiente manera:
# my_important_option = config.get_main_option("my_important_option") ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
