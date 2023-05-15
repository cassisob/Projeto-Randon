from pydantic import BaseModel

class Time(BaseModel):
    nome : str
    cidade : str

    class Config():
        orm_mode = True
    
class Jogador(BaseModel):
    nome : str
    nick : str
    patente : str
    funcao : str
    steam : str
    gamersClub : str
    time_id : int

    class Config():
        orm_mode = True

class Coach(BaseModel):
    nome : str
    nick : str
    time_id : int

    class Config():
        orm_mode = True