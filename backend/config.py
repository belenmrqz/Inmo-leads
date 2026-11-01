from pydantic_settings import BaseSettings, SettingsConfigDict

# ESTE ARCHIVO LEE LA CONFIGURACIÓN DEL PROYECTO

class Settings(BaseSettings): # Guarda la dirección de la bbdd de .env
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings() # Instancia única que importa el resto del código