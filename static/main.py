from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.staticfiles import StaticFiles

class TarefaIn(BaseModel): #o que o cliente envia 
    titulo: str = Field(min_length=3, max_length=100)
    prioridede: int = Field(ge=1, le=5)   # ge = >=, le = <=

class Tarefa(TarefaIn):                   # o que a API devolve
    id: int
    concluida: bool = False

app = FastAPI(title="API de Tarefas")
tarefas: list[Tarefa] = []

@app.get("/api/tarefas")
def listar_tarefas() -> list[Tarefa]:
    return tarefas

@app.post("/api/tarefas", status_code=201)
def criar_tarefa(dados: TarefaIn) -> Tarefa:
    tarefa = Tarefa(id=len(tarefa) + 1, **dados.model_dump())
    tarefas.append(tarefa)
    return tarefa

@app.get("/api/tarefas/{id}")
def buscar_tarefa(id: int) -> Tarefa:
    for tarefa in tarefas:
        if tarefa.id == id:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.get("/api/ola")
def ola():
    return{"mensagem": "Olá, mundo!"}

app.mount("/", StaticFiles(directory="static",html=True), name="static")
