from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuario/<nome_usuario>;<nome_profissao>')
@app.route('/usuario', defaults={'nome_usuario':'usuario?', 'nome_profissao':''})   #Valores padrão para os argumentos.
def usuario(nome_usuario, nome_profissao):
    dados_usuario = {'profissao':nome_profissao, 'disciplina':'Desenvolvimento para Web III'}
    return render_template('usuario.html', nome_usuario=nome_usuario, dados_usuario=dados_usuario)

if __name__ == '__main__':
    app.run()