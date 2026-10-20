"""API de tarefas em memoria (FastAPI).
EndPoints: GET /tarefas POST /tarefas"""

from fastapi import FastAPI, status
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(title="API de tarefas", version="1.0.0")

#Armazenamento em memória. Será perdido quando o container reinicia
_tarefas: list[dict] = []

class tarefaEntrada(BaseModel):
    titulo : str = Field(min_length=1, max_length=120)

class Tarefa(BaseModel):
    id: int
    titulo:str

app.get("/tarefas", response_model=list[Tarefa])
def listar_tarefas():
    return _tarefas

@app.post("/tarefas", response_model=Tarefa,
status_code=status.HTTP_201_CREATED)
def criar_tarefa(entrada:Tarefa):
    tarefa={
        "id": len(_tarefas)+1,
        "titulo": entrada.titulo
    }
    _tarefas.append(tarefa)
    return tarefa

"""if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
    reload=True)"""