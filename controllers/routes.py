from flask import render_template, request

funcoes = []

titulares = []

gamelist = [{'Título' : 'CS-GO', 'Ano' : 2012, 'Categoria' : 'FPS Online'}]

timelist = [{'Nome': 'Neymar', 'Funcao' : 'atacante'}]

def init_app(app):
    # Definindo a rota principal
    @app.route('/')
    # Função que será executada ao acessar a rota
    def home():
        # Retorno que será exibido na rota
        return render_template('index.html')
    
    @app.route('/cadastro_titulares', methods=['GET', 'POST'])
    def cadastro_titulares():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('funcao'):
                gamelist.append({'Nome': request.form.get('nome'), 'Funcao' : request.form.get('funcao')})
        
        return render_template('cadgames.html', timelist=timelist)
    
    @app.route('/times', methods=['GET','POST'])
    def times():
        time = timelist[0]

        if request.method == 'POST':
            if request.form.get('titular'):
                titulares.append(request.form.get('titular'))

            if request.form.get('funcao'):
                funcoes.append(request.form.get('funcao'))
        return render_template('times.html', time=time, titular=titular, funcao=funcao)

    @app.rout('/historia', methods=['GET', 'POST'])
    def historia():
        return render_template('historia.html')            