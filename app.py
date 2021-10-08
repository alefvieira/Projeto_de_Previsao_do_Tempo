from flask import Flask, render_template, request
import comandos_BD
import requests

app = Flask(__name__)


@app.route('/')
def index():
    comandos_BD.atualizarValores()
    return render_template('index.html')

@app.route('/graficos', methods=['GET', 'POST'])
def pag_graficos():
    # vai pegar o valor da requisição ajax e va converter o dado recebido do tipo byetes em tipo string
    # tygrafico = request.get_data()
    # converte = tygrafico.decode("utf-8")
    # converte = converte.replace('tygrafico=', '')
    # comandos_BD.query_cria_grafico(converte)
    return render_template('secao_graficos.html')   


if __name__ == "__main__":
    # app.run()
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)


