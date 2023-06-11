from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

clientes = {}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/clientes')
def listar_clientes():
    return render_template('clientes.html', clientes=clientes)


@app.route('/cadastrar-cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        cliente_id = len(clientes) + 1
        clientes[cliente_id] = {'nome': nome, 'endereco': endereco, 'telefone': telefone}
        return redirect(url_for('listar_clientes'))
    return render_template('cadastrar_cliente.html')


@app.route('/ver-cliente/<int:id>')
def ver_cliente(id):
    cliente = clientes.get(id)
    if cliente:
        return render_template('ver_cliente.html', cliente=cliente)
    return 'Cliente não encontrado.'


@app.route('/editar-cliente/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = clientes.get(id)
    if not cliente:
        return 'Cliente não encontrado.'

    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        clientes[id] = {'nome': nome, 'endereco': endereco, 'telefone': telefone}
        return redirect(url_for('listar_clientes'))
    return render_template('editar_cliente.html', cliente=cliente)


@app.route('/excluir-cliente/<int:id>', methods=['POST'])
def excluir_cliente(id):
    cliente = clientes.get(id)
    if not cliente:
        return 'Cliente não encontrado.'
    del clientes[id]
    return redirect(url_for('listar_clientes'))


if __name__ == '__main__':
    app.run(debug=True)
