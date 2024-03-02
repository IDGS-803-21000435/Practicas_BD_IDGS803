from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
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