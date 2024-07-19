import requests # Biblioteca usada para fazer requisições http em python
from bs4 import BeautifulSoup

url = 'https://www.w3schools.com'
resposta = requests.get(url) #Envia uma requisição Get para obter o conteúdo da página

soup = BeautifulSoup(resposta.text, 'html.parser') 
#Cria um objeto chamado soup que recebe como argumentos o conteúdo html. 

#html.parser = permite extrair informações da página web de forma mais fácil e estruturada.
titulos = soup.find_all('h4')

for titulo in titulos:
    print(titulos)