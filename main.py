from fastapi import FastAPI
from Banco.database import Base, engine
from Rotas import times, jogadores
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(times.router)
app.include_router(jogadores.router)

origins=["*"]

app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)