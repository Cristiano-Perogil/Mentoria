from dto.carroDTO import Carro
import uvicorn
from fastapi import FastAPI

api = FastAPI()


@api.get("/news")
def main():
    return gettingData()


@api.post('/carro/cor')
def mudaCor(carro: Carro) -> str:
    return f"O carro {carro.id} modou de cor para {carro.cor}"


if __name__ == "__main__":
    uvicorn.run("app:api", host="0.0.0.0", port=8080, reload=True)
