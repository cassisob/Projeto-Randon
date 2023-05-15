from fastapi import APIRouter, Depends, Response, status, HTTPException

from Rotas import utils
from Banco.database import SessionLocal, get_db
from Banco import models, schemas

from typing import Optional

router = APIRouter(
    tags = ['Times'],
    prefix = '/times'
)

@router.get('/')
def list_all(search : Optional[str] = "", db: SessionLocal = Depends(get_db)):
    if search != "":
        times = db.query(models.Time).filter(models.Time.nome.contains(search)).all() #retorna os times solicitados a partir do nome na url
    else:
        times = db.query(models.Time).all() #como não tem id na url, retorna todos os times cadastrados
    return times

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Time, db: SessionLocal = Depends(get_db)):
    novo_time = models.Time(nome=request.nome, cidade=request.cidade)

    db.add(novo_time)
    db.commit()
    db.refresh(novo_time)

    return novo_time