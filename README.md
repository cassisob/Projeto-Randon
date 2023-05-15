# Projeto-Randon

Projeto de teste by @cassisob

Para rodar o projeto intale as seguintes biliotecas com pip:

1. pip install fastapi
2. pip install uvicorn
3. pip install sqlalchemy

O projeto conta com 3 frentes:
    <li>1. Banco de Dados</li>
      
              Table Times

                1. nome : str
                2. cidade : str
                3. id : int (chave primaria)

              Table Jogador

                1. nome : str
                2. nick : str
                3. patente : str
                4. funcao : str
                5. steam : str
                6. gamersClub : str
                7. time_id : int (chave estranjeira para relacionar o jogador com o time)
                8. id : int (chave primaria)

             Table Coach

                1. nome : str
                2. nick : str
                3. time_id : int (chave estranjeira para relacionar o jogador com o time)
                4. id : int (chave primaria)
    
   
   <li> 2. API </pi>
   
            API feita em Python com FASTAPI com as seguintes rotas
                
            http://localhost:8000/times/
            1. Método GET: Podemos solicitar todos os times cadastrados no banco de dados e com a extensão "?search=PALAVRA" na URL podemos pesquisar por times especificos com a "palavra" como nome </li>
            2. Método POST: Podemos adicionar adicionar times no banco de dados com o formato de JSON abaixo

                  1.     {
                  2.       "nome": "string",
                  3.        "cidade": "string"
                  4.      }

            3. Método DELETE: Podemos deletar uma equipe do banco de dados, enviando o id da mesma na url após "times/"
            4. Não foi criado o método PUT devido ao tamanho decidido do projeto durante a fase de idealização 
             
            http://localhost:8000/jogadores/
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
            4. Não foi criado o método PUT devido ao tamanho decidido do projeto durante a fase de idealização 
            
            Devido ao tamanho do projeto, não foi criado a rota de cadastrar coachs.
    
  <li> 3. Página WEB </li>
              
            A pagina WEB foi criada a fim de cadastrar times e jogadores dentro do banco de dados.
            Nela podemos ver um ambiente bonito e com muitos elementos de JavaScript.
                
