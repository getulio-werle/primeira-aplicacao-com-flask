from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = 'password'

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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    #Método GET:
    #usuario = request.args.get('nome_usuario')
    #senha = request.args.get('senha')
    #return f'Usuário: {usuario} e Senha: {senha}'
    #Método POST:
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    if usuario == 'admin' and senha == 'ifro':     #Teste de condição para fazer login.
        return f'Usuário: {usuario} e Senha: {senha}'
    else:
        flash("Dados inválidos.")   #Caso não sejam os argumentos esperados redireciona para /login
        return redirect('/login')

if __name__ == '__main__':
    app.run()