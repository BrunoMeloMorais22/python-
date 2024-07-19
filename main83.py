from flask import Flask # Importa a classe Flask necessário para a criação de páginas web em python

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/') # Define uma rota Flask
def index():
    return 'Hello, World!. This is my first application web in python'

if __name__ == '__main__': #Verifica se o script está sendo executado diretamente
    app.run()
