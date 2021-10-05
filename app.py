from flask import Flask, render_template
import comandos_BD as tes
import comandos_BD
app = Flask(__name__)


@app.route('/')
def index():
    
    comandos_BD.atualizarValores()
    return render_template('index.html')

@app.route('/graficos')
def pag_graficos():
    return render_template('secao_graficos.html')   

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)

app.run()


