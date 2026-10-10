from datetime import date

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API Achados e Perdidos")


# ---------- Modelos ----------

class ObjetoEntrada(BaseModel):
    """Dados enviados no cadastro (o id e gerado pela API)."""
    descricao: str
    local: str
    data: date              # formato: "2026-10-10"
    status: str = "perdido"  # ex.: perdido, encontrado, devolvido


class Objeto(ObjetoEntrada):
    """Objeto completo, com id."""
    id: int


# ---------- "Banco de dados" em memoria ----------

objetos: dict[int, Objeto] = {}
proximo_id = 1


def buscar_ou_404(id: int) -> Objeto:
    if id not in objetos:
        raise HTTPException(status_code=404, detail=f"Objeto {id} nao encontrado")
    return objetos[id]


# ---------- Rotas ----------

@app.get("/objetos", response_model=list[Objeto])
def obter_todos():
    """GET /objetos -> obter todos os objetos."""
    return list(objetos.values())


@app.get("/objeto", response_model=Objeto)
def obter_um(id: int):
    """GET /objeto?id=1 -> obter um objeto."""
    return buscar_ou_404(id)


@app.post("/objeto", response_model=Objeto, status_code=201)
def cadastrar(dados: ObjetoEntrada):
    """POST /objeto -> cadastrar um objeto."""
    global proximo_id
    novo = Objeto(id=proximo_id, **dados.model_dump())
    objetos[novo.id] = novo
    proximo_id += 1
    return novo


@app.put("/objeto", response_model=Objeto)
def atualizar(dados: Objeto):
    """PUT /objeto -> atualizar um objeto (o id vai no corpo do JSON)."""
    buscar_ou_404(dados.id)
    objetos[dados.id] = dados
    return dados


@app.delete("/objeto")
def excluir(id: int):
    """DELETE /objeto?id=1 -> excluir um objeto."""
    buscar_ou_404(id)
    del objetos[id]
    return {"mensagem": f"Objeto {id} excluido com sucesso"}
