from pydantic import BaseModel


class Carro(BaseModel):
    id: str
    cor: str
