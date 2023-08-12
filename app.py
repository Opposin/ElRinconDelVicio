from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

direccion_archivo = os.path.abspath(os.getcwd())+"\database\datos.db"
app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+direccion_archivo
db = SQLAlchemy(app)

class juego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True)
    descripcion = db.Column(db.String(500))
    imagen = db.Column(db.String(50))
    fecha_lanzamiento = db.Column(db.Date, default=datetime.utcnow)
    
    def __init__(self, nombre, descripcion, imagen, fecha_lanzamiento):
        self.nombre = nombre
        self.descripcion = descripcion
        self.imagen = imagen
        self.fecha_lanzamiento = fecha_lanzamiento
    

@app.route('/')
def index():
    juegos = juego.query.all()
    return render_template('index.html', juegos = juegos)

@app.route('/login')
def login():
    juegos = juego.query.all()
    return render_template('Login.html', juegos = juegos)

@app.route('/nosotros')
def nosotros():
    juegos = juego.query.all()
    return render_template('nosotros.html', juegos = juegos)

@app.route('/juego', methods=['GET'])
def visualizar_juego():
    juegos = juego.query.all()
    return render_template('index.html', juegos = juegos)

@app.route('/cjuegos')
def creacion_juegos():
    juegos = juego.query.all()
    return render_template('cjuegos.html', juegos = juegos)

@app.route('/crear_juego', methods=['POST'])
def crear_juego():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    imagen = request.form['imagen']
    fecha = request.form['fecha_lanzamiento']
    fecha_lanzamiento = datetime.strptime(fecha,'%Y-%m-%d')
    entrada = juego(nombre, descripcion,imagen , fecha_lanzamiento)
    try:
        db.session.add(entrada)
        db.session.commit()
        return redirect(url_for('creacion_juegos'))
    except:
        return "no se pudo guardar"


@app.route('/delete/<id>')
def delete(id):
    juego.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('creacion_juegos'))

    
if __name__ == '__main__':
    app.run(debug=True)
    
