from typing import Optional
from sqlmodel import Field, SQLModel

class Usuario(SQLModel, table=True):
    id_usuario: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    tipo_conta: str
    senha_mestre: Optional[str] = None
    chave_totp: Optional[str] = None

class Dispositivo(SQLModel, table=True):
    id_dispositivo: Optional[int] = Field(default=None, primary_key=True)
    modelo_aparelho: str
    ip_tailscale: str
    status_seguranca: bool = Field(default=False)
    
    # Aqui é a Chave Estrangeira que amarra o aparelho ao dono
    id_usuario: Optional[int] = Field(default=None, foreign_key="usuario.id_usuario")