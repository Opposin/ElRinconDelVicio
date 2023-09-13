from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user, login_required
from datetime import datetime
import os

direccion_archivo = os.path.abspath(os.getcwd())+"\database\datos.db"
app = Flask(__name__)
app.secret_key = 'hihi2475'
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+direccion_archivo
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

#modelo de usuario admin
class User(UserMixin):
    def __init__(self, usuario, contrasenia):
        self.usuario = usuario
        self.contrasenia = contrasenia
        
    def get_id(self):
        return self.usuario
    
#modelo de datos de cada juego
class juego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True)
    descripcion = db.Column(db.String(500))
    sistema_juego = db.Column(db.String(50))
    imagen = db.Column(db.String(200))
    url_gameplay = db.Column(db.String(200), default="null")
    fecha_lanzamiento = db.Column(db.Date, default=datetime.utcnow)
    
    def __init__(self, nombre, descripcion, sistema_juego, imagen, url_gameplay, fecha_lanzamiento):
        self.nombre = nombre
        self.descripcion = descripcion
        self.sistema_juego = sistema_juego
        self.imagen = imagen
        self.url_gameplay = url_gameplay
        self.fecha_lanzamiento = fecha_lanzamiento

@login_manager.user_loader
def load_user(user_id):
    return user if user.get_id() ==  user_id else None

#cuenta usuario admin
user = User('admin', '1234')

login_manager.user_loader(load_user)

#ruta para el index de la pagina      
@app.route('/')
def index():
    juegos = juego.query.all()
    return render_template('index.html', juegos = juegos)

#ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        logout_user()
        return redirect('/')
    
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']
        
        if user.usuario == usuario and user.contrasenia == contrasenia:
            login_user(user)
            return redirect('/')
    
        return render_template('LoginE.html')    
    
    return render_template('Login.html')

#ruta about-us
@app.route('/nosotros')
def nosotros():
    juegos = juego.query.all()
    return render_template('nosotros.html', juegos = juegos)

#ruta visualizacion de juego individual
@app.route('/juego/<id>', methods=['GET'])
def visualizar_juego(id):
    game = juego.query.get(id)
    return render_template('juego.html', game = game)

@app.route('/compra/<int:id>', methods=['GET'])
def visualizar_compra(id):
    game = juego.query.get(id)
    return render_template('compra.html', game = game)

@app.route('/comprado/<int:id>', methods=['GET'])
def visualizar_producto(id):
    game = juego.query.get(id)
    return render_template('comprado.html', game = game)

#ruta pagina general para ajustes de catalogo
@app.route('/cjuegos')
@login_required
def creacion_juegos():
    juegos = juego.query.all()
    return render_template('cjuegos.html', juegos = juegos)

#ruta para la creacion de un juego
@app.route('/crear_juego', methods=['POST'])
@login_required
def crear_juego():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    sistema_juego = request.form['sistema_juego']
    imagen = request.form['imagen']
    url_gameplay = request.form['url_gameplay']
    fecha = request.form['fecha_lanzamiento']
    fecha_lanzamiento = datetime.strptime(fecha,'%Y-%m-%d')
    entrada = juego(nombre, descripcion, sistema_juego, imagen, url_gameplay, fecha_lanzamiento)
    try:
        db.session.add(entrada)
        db.session.commit()
        return redirect(url_for('creacion_juegos'))
    except:
        return "no se pudo guardar"

#Ruta para la modificacion de un juego
@app.route('/mjuego/<int:id>', methods=['GET'])
@login_required
def modificar_juego(id):
    game = juego.query.get(id)
    return render_template('mjuegos.html', game = game)

#ruta para la realizar la modificacion del juego
@app.route('/modificar_juego/<int:id>', methods=['GET', 'POST'])
@login_required
def modificacion_juego(id):
    id_a_actualizar = juego.query.filter_by(id = id).first()
    if request.method == "POST": 
        id_a_actualizar.nombre = request.form['nombre']
        id_a_actualizar.descripcion = request.form['descripcion']
        id_a_actualizar.sistema_juego = request.form['sistema_juego']
        id_a_actualizar.imagen = request.form['imagen']
        id_a_actualizar.url_gameplay = request.form['url_gameplay']
        fecha = request.form['fecha_lanzamiento']
        id_a_actualizar.fecha_lanzamiento = datetime.strptime(fecha,'%Y-%m-%d')
        db.session.commit()
        return redirect(url_for('creacion_juegos'))

#ruta para la eliminacion de un jugo
@app.route('/delete/<id>')
@login_required
def delete(id):
    juego.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('creacion_juegos'))

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Usted no tiene accesso a esta pagina, debe logear.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
