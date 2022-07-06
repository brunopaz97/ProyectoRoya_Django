from pipes import Template
from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):

    def __init__(self, nombre):
        
        self.nombre=nombre


def index(request):

    p1=Persona("Alejandro")
    nombre="Bruno"
    temasdelcurso=["Plantillas", "Modelos", "Formularios", "Vistas","Despliegue"]

    fecha_actual=datetime.datetime.now()

    #doc_externo=open("C:/Users/Coodinacion_03/Desktop/PAZ/ProyectosDjango/ProyectoRoya/ProyectoRoya/plantillas/index.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()

    #doc_externo=get_template('index.html')
    ctx={"nombre_persona" : nombre , "fecha_actual" : fecha_actual, "temas":temasdelcurso}
    #documento=doc_externo.render(ctx)

    return render(request, "index.html", ctx)


#View para el ingreso de datos / formulario
def ingresodatos(request):
    
    #doc_ingreso_datos=open("C:/Users/Coodinacion_03/Desktop/PAZ/ProyectosDjango/ProyectoRoya/ProyectoRoya/plantillas/formulario_ingreso_datos.html", encoding="utf8")

    #plt=Template(doc_ingreso_datos.read())

    #doc_ingreso_datos.close()

    #ctx=Context()

    #documento_ingreso_datos=plt.render(ctx)

    #return HttpResponse(documento_ingreso_datos)

    return render(request, 'formulario_ingreso_datos.html')


#View para los gauges




def finish(request):

    doc_index1=open("C:/Users/Coodinacion_03/Desktop/PAZ/ProyectosDjango/ProyectoRoya/ProyectoRoya/plantillas/index1.html", encoding="utf8")

    plt=Template(doc_index1.read())

    doc_index1.close()

    ctx=Context()

    documento_index1=plt.render(ctx)

    return HttpResponse(documento_index1)


def verfecha(request):

    fecha_actual=datetime.datetime.now()

    doc="""
    <!DOCTYPE html>
    <html>
    <body>
        <h2>Fecha y Hora actuales %s</h2>
    </body>
    </html>
    """ % fecha_actual

    return HttpResponse(doc)


def calculaEdad(request, agno):

    edadActual=25
    periodo=agno-2022
    edadFutura=edadActual+periodo
    doc="""
    <!DOCTYPE html>
    <html>
    <body>
        <h2>En el años %s tendrás %s años</h2>
    </body>
    </html>
    """ %(agno, edadFutura)
    return HttpResponse(doc)