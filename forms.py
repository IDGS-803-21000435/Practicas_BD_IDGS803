from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField, DateField, BooleanField
from wtforms import validators


class Empleado(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre',[
        validators.DataRequired(message='elcampo es requerido'),
        validators.length(min=4, max=10, message='ingresa nombre valido')
    ])
    correo = EmailField('Correo', [
        validators.Email(message='Ingrese un correo valido'),
    ])
    telefono = StringField('Telefono', [
        validators.DataRequired(message='elcampo es requerido'),
        validators.length(min=4, max=10, message='ingresa nombre valido')
    ])
    direccion = StringField('Direccion',[
        validators.DataRequired(message='elcampo es requerido'),
        validators.length(min=4, max=10, message='ingresa nombre valido')
    ])
    sueldo = IntegerField('Sueldo', [
        validators.number_range(min=1, max=20, message='valor no valido')
    ])

# ------------ PRACTICA PIZZA ---------------------        
class pizzaForm(Form):
    id = IntegerField('idPizza')
    tamanio = RadioField('Tamaño de pizza', choices=[('Chica','Chica $40'), ('Mediana', 'Mediana $80'), ('Grande', 'Grande $120')])
    jamon = BooleanField('Jamon')
    pinia = BooleanField('Piña')
    champiniones = BooleanField('Champiñones')
    no_pizza = IntegerField('Numero de pizzas')
    nombreCompleto = StringField('Nombre Completo')
    direccion = StringField('Direccion')
    telefono = StringField('Telefono')
    fechaCompra = DateField('Fecha de compra')
    
# ------------------------------------------------------