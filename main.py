from flask import Flask, render_template, request, flash, Response, redirect
from flask_wtf.csrf import CSRFProtect
import forms
from flask import g

from models import db
from models import PracticaBD, pizzaModel, clientePizzaModel
from config import DevelopmentConfig, DevelopmentConfigPizza

app = Flask(__name__)
app.secret_key = 'clave_secreta'
app.config.from_object(DevelopmentConfigPizza)

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


@app.route("/indexPizza", methods=["GET","POST"])
def indexPizza():
    form_Pizza = forms.pizzaForm(request.form)
    
    if request.method == 'POST':#and alum_form.validate()
        jamon = ''
        champi = ''
        pinia = ''
        
        if form_Pizza.jamon.data:
            jamon += 'jamon'
        
        if form_Pizza.champiniones.data:
            champi += 'champiñones'
        
        if form_Pizza.pinia.data:
            pinia += 'pinia'
        
        pizza = pizzaModel(
            tam = form_Pizza.tamanio.data,
            ingredientes = jamon + " " + champi + " " + pinia,
            No_pizzas = form_Pizza.no_pizza.data
        )
        
        cliente = clientePizzaModel(
            nombre = form_Pizza.nombreCompleto.data,
            direccion = form_Pizza.direccion.data,
            telefono = form_Pizza.telefono.data,
            fecha = form_Pizza.fechaCompra.data
        )
        
        db.session.add(cliente)
        db.session.add(pizza)
        db.session.commit()
         
    return render_template("indexPizza.html", formPizza = form_Pizza)


@app.route("/eliminar", methods=["GET","POST"])
def eliminar():
    alum_form = forms.Empleado(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(PracticaBD).filter(PracticaBD.id == id).first()
        
        
    if request.method == 'POST':
        id = alum_form.nombre.id
        alum = PracticaBD.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect('ABC_Completo')
    
    return render_template("eliminar.html", form = alum_form)


@app.route("/modificar", methods=["GET","POST"])
def modificar():
    alum_form = forms.Empleado(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(PracticaBD).filter(PracticaBD.id == id).first()
        alum_form.id.data = request.args.get('id')
        alum1.nombre = alum_form.nombre.data
        alum1.correo = alum_form.correo.data
        alum1.telefono = alum_form.telefono.data
        alum1.direccion = alum_form.direccion.data
        alum1.sueldo = alum_form.sueldo.data
        
    if request.method == 'POST':
        id = alum_form.id.data
        alum1 = db.session.query(PracticaBD).filter(PracticaBD.id == id).first()
        alum1.nombre = alum_form.nombre.data
        alum1.correo = alum_form.correo.data
        alum1.telefono = alum_form.telefono.data
        alum1.direccion = alum_form.direccion.data
        alum1.sueldo = alum_form.sueldo.data
        db.session.commit()
        return redirect('ABC_Completo')
    
    return render_template("modificar.html", form = alum_form)


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
