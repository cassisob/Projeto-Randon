from Banco import models
from fastapi import status, HTTPException

def checarTimePorID(id, db):
    query = db.query(models.Time).filter(models.Time.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'time com o id {id} não foi encontrado')
    return query

def checarJogadorPorID(id, db):
    query = db.query(models.Jogador).filter(models.Jogador.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'jogador com o id {id} não foi encontrado')
    return query
