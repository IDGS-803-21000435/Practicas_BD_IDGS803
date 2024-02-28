from flask import Flask, render_template, request, flash, Response, redirect
from flask_wtf.csrf import CSRFProtect
import forms
from flask import g

from models import db
from models import PracticaBD
from config import DevelopmentConfig

app = Flask(__name__)
app.secret_key = 'clave_secreta'
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()


@app.route("/index", methods=["GET","POST"])
def index():
    alum_form = forms.Empleado(request.form)
    if request.method == 'POST':#and alum_form.validate()
        alum = PracticaBD(
        nombre = alum_form.nombre.data,
        correo = alum_form.correo.data,
        telefono = alum_form.telefono.data,
        direccion = alum_form.direccion.data,
        sueldo = alum_form.sueldo.data
        )
        
        db.session.add(alum)
        db.session.commit()
         
    return render_template("index.html", form = alum_form)


@app.route("/ABC_Completo", methods=["GET","POST"])
def ABC_Completo():
    
    alumno = PracticaBD.query.all()

    return render_template("ABC_Completo.html", alumnos = alumno)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.nombre = 'Daniel'
    print('before_request')
    
    
@app.after_request
def after_request(response):
    print('after_request')
    if 'Daniel' not in g.nombre and request.endpoint not in['/index']:
        return redirect('index.html')
    return response
    
# ------------------------------------------------------------
if __name__ =="__main__":
    csrf.init_app(app)  #se utiliza debug = True para ctivar "actualizaciones en caliente" similar liveServer
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
#   para tumbar el servidor es con el comando ctrl + c
#   para activarlo se ejecuta el archivo, escribir en la terminal "py nombre.py"
#   nombre, correo, Telefono, Sueldo
