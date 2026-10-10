# CMP2304/C02 — Atividade Bônus (10/10/2026)

**API REST — Achados e Perdidos**

API para gerenciar itens perdidos e encontrados, permitindo cadastrar, consultar,
atualizar e excluir objetos.

Os dados ficam **em memória do servidor** (um dicionário Python), ou seja, são
**perdidos ao reiniciar a aplicação**. Não há banco de dados.

## Como rodar

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Testar no navegador (Swagger): http://127.0.0.1:8000/docs

## Endpoints

| Método | Rota            | Descrição                |
| ------ | --------------- | ------------------------ |
| GET    | `/objetos`      | Obter todos os objetos   |
| GET    | `/objeto?id=1`  | Obter um objeto          |
| POST   | `/objeto`       | Cadastrar um objeto      |
| PUT    | `/objeto`       | Atualizar um objeto      |
| DELETE | `/objeto?id=1`  | Excluir um objeto        |

## Modelo do objeto

| Campo       | Tipo   | Observação                                      |
| ----------- | ------ | ----------------------------------------------- |
| `id`        | int    | Gerado pela API no cadastro                     |
| `descricao` | string | —                                               |
| `local`     | string | —                                               |
| `data`      | date   | Formato `AAAA-MM-DD`                            |
| `status`    | string | Padrão `"perdido"`; ex.: encontrado, devolvido  |

## Exemplos

Corpo do `POST /objeto` (sem `id` — ele é gerado pela API):

```json
{
  "descricao": "Guarda-chuva preto",
  "local": "Bloco C, sala 204",
  "data": "2026-10-10",
  "status": "perdido"
}
```

Corpo do `PUT /objeto` (o `id` vai no corpo do JSON):

```json
{
  "id": 1,
  "descricao": "Guarda-chuva preto",
  "local": "Bloco C, sala 204",
  "data": "2026-10-10",
  "status": "devolvido"
}
```
