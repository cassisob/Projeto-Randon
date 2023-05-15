from fastapi import APIRouter, Depends, Response, status, HTTPException

from Rotas import utils
from Banco.database import SessionLocal, get_db
from Banco import models, schemas

from typing import Optional

router = APIRouter(
    tags = ['Jogadores'],
    prefix = '/jogadores'
)

@router.get('/')
def list_all(search : Optional[str] = "", db: SessionLocal = Depends(get_db)):
    if search != "":
        jogadores = db.query(models.Jogador).filter(models.Time.nome.contains(search)).all()

    else:
        jogadores = db.query(models.Jogador).all()
    return jogadores


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Jogador, db: SessionLocal = Depends(get_db)):

    utils.checarTimePorID(request.time_id, db)

    novo_jogador = models.Jogador(
        nome=request.nome,
        nick=request.nick,
        patente=request.patente,
        funcao=request.funcao,
        steam=request.steam,
        gamersClub=request.gamersClub,
        time_id=request.time_id
        )
    
    db.add(novo_jogador)
    db.commit()
    db.refresh(novo_jogador)

    return novo_jogador

@router.delete('/{id}')
def destroy(id: int, db: SessionLocal = Depends(get_db)):
    query = utils.checkLivroById(id, db)
    
    query.first().autores = []

    query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
