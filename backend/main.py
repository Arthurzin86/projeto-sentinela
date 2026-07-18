from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from models import Usuario, Dispositivo # Importando as tabelas que fizemos na mão

# 1. Inicializando o servidor
app = FastAPI(title="API Sentinela")

# 2. Criando o motor do banco de dados (Vamos usar SQLite para a fase de testes local)
sqlite_url = "sqlite:///./sentinela.db"
engine = create_engine(sqlite_url, echo=True)

# 3. Função para construir as tabelas no momento em que o servidor ligar
@app.on_event("startup")
def criar_banco():
    SQLModel.metadata.create_all(engine)
    print("Banco de dados criado e tabelas montadas com sucesso!")

# 4. Primeira Rota (Apenas para testar se o servidor está vivo)
@app.get("/")
def ler_raiz():
    return {"status": "Servidor Sentinela Operacional e Blindado"}