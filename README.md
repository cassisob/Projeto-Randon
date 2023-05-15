# Projeto-Randon

Projeto de teste by @cassisob

Para rodar o projeto intale as seguintes biliotecas com pip:

1. pip install fastapi
2. pip install uvicorn
3. pip install sqlalchemy

O projeto conta com 3 frentes:
  1. Banco de Dados
      <ol>Banco de dados com os seguintes dados:
        <li>Table Times </li>
        
          1. nome : str
          2. cidade : str
          3. id : int (chave primaria)
        <li>Table Jogador </li>
        
          1. nome : str
          2. nick : str
          3. patente : str
          4. funcao : str
          5. steam : str
          6. gamersClub : str
          7. time_id : int (chave estranjeira para relacionar o jogador com o time)
          8. id : int (chave primaria)
       <li>Table Coach </li>
       
          1. nome : str
          2. nick : str
          3. time_id : int (chave estranjeira para relacionar o jogador com o time)
          4. id : int (chave primaria)
  <ol>
  2. API
      <li>http://localhost:8000/times/ </li>
        
            1. Método GET: Podemos solicitar todos os times cadastrados no banco de dados e com a extensão "?search=PALAVRA" na URL podemos pesquisar por times especificos com a "palavra" como nome </li>
            2. Método POST: Podemos adicionar adicionar times no banco de dados com o formato de JSON abaixo
    
          1.     {
          2.       "nome": "string",
          3.        "cidade": "string"
          4.      }
    
            3. Método DELETE: Podemos deletar uma equipe do banco de dados, enviando o id da mesma na url após "times/"
 Não foi criado o método PUT devido ao tamanho decidido do projeto durante a fase de idealização 
    <li> http://localhost:8000/jogadores/ </li>
    
            1. Método GET: Podemos solicitar todos os jogadores cadastrados no banco de dados e com a extensão "?search=PALAVRA" na URL podemos pesquisar por jogadores especificos com a "palavra" como nome
            2. Método POST: Podemos adicionar adicionar jogadores no banco de dados com o formato de JSON abaixo
    
          1. {
          2.   "nome": "string",
          3.   "nick": "string",
          4.   "patente": "string",
          5.   "funcao": "string",
          6.   "steam": "string",
          7.   "gamersClub": "string",
          8.   "time_id": 0
          9. }     
    
            3. Método DELETE: Podemos deletar um jogador do banco de dados, enviando o id do mesmo na url após "jogadores/"
 
          
          
 Não foi criado o método PUT devido ao tamanho decidido do projeto durante a fase de idealização 
