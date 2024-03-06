from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PracticaBD(db.Model):
    __tablename__= 'Empleado'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    sueldo = db.Column(db.Integer)

# ------------ PRACTICA PIZZA ---------------------
class pizzaModel(db.Model):
    __tablename__= "Pizza"
    id = db.Column(db.Integer, primary_key = True)
    tam = db.Column(db.String(100))
    ingredientes = db.Column(db.String(50))
    No_pizzas = db.Column(db.Integer)
    
class clientePizzaModel(db.Model):
    __tablename__= 'Cliente'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    fecha = db.Column(db.Date())
# -----------------------------------------------------