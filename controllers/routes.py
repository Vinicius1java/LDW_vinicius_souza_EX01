from flask import render_template

def init_app(app):
    
    @app.route('/')

    def home():
        return render_template('index.html')

    @app.route('/titulos')
    def titulos():
        titulo = 'Campeonato santista de 1913'
        ano = 1913
        return render_template('titulos.html',titulo=titulo, ano=ano)

    @app.route('/jogadores')
    def jogador():
        jogador = ['Neymar','Ganso']
        contratacao = ['2009','2005']
        return render_template('jogadores.html',jogador=jogador,contratacao=contratacao)