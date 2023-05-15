# Projeto-Randon

Projeto de teste by @cassisob

Para rodar o projeto intale as seguintes biliotecas com pip:

1. pip install fastapi
2. pip install uvicorn
3. pip install sqlalchemy

O projeto conta com 3 frentes:
  1. Banco de Dados
      Banco de dados com os seguintes dados: \n
        a. Table Times
        
          1. nome : str
          2. cidade : str
          3. id : int (chave primaria)
        b. Table Jogador
        
          1. nome : str
          2. nick : str
          3. patente : str
          4. funcao : str
          5. steam : str
          6. gamersClub : str
          7. time_id : int (chave estranjeira para relacionar o jogador com o time)
          8. id : int (chave primaria)
       c. Table Coach
       
          1. nome : str
          2. nick : str
          3. time_id : int (chave estranjeira para relacionar o jogador com o time)
          4. id : int (chave primaria)
  
  2. API
