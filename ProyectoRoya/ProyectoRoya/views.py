from pipes import Template
from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

from plotly.offline import plot
import plotly.graph_objects as go

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


def demo_plot_view(request):

    x = [i for i in range (-10, 11)]
    y1 = [3*i for i in x]
    y2 = [i**2 for i in x]
    y3 = [10*abs(i) for i in x]

    graphs = []

    graphs.append(
        go.Scatter(x=x, y=y1, mode='lines', name='Line y1')
    )

    graphs.append(
        go.Scatter(x=x, y=y2, mode='markers', opacity=0.8, 
                   marker_size=y2, name='Scatter y2')
    )
    
    graphs.append(
        go.Bar(x=x, y=y3, name='Bar y3')
    )

    layout = {
        'title': 'Title of the figure',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 420,
        'width': 560,
    }

    plot_div = plot({'data': graphs, 'layout': layout}, output_type='div')

    return render(request, 'demo-plot.html', context={'plot_div': plot_div})

def gauge_view(request):

    #Gauge de Temperatura
    fig_temp = go.Figure(go.Indicator(
            domain = {'x': [0, 1], 'y': [0, 1]},
            value = 24,
            mode = "gauge+number+delta",
            title = {'text': "Temperatura (°C)"},
            delta = {'reference': 22},
            gauge = {'axis': {'range': [None, 40]},
                    'steps' : [
                        {'range': [0, 17], 'color': "beige"},
                        {'range': [17, 27], 'color': "lime"},
                        {'range': [27, 40], 'color': "orangered"}]}))

    #Gauge de Precipitación
    fig_prec = go.Figure(go.Indicator(
            domain = {'x': [0, 1], 'y': [0, 1]},
            value = 107,
            mode = "gauge+number+delta",
            title = {'text': "Precipitación Acumulada (mm)"},
            delta = {'reference': 125},
            gauge = {'axis': {'range': [None, 200]},
                    'steps' : [
                        {'range': [0, 100], 'color': "beige"},
                        {'range': [100, 180], 'color': "lime"},
                        {'range': [180, 200], 'color': "orangered"}]}))
 

    #Gauge de Radiación
    fig_rad = go.Figure(go.Indicator(
            domain = {'x': [0, 1], 'y': [0, 1]},
            value = 1367,
            mode = "gauge+number+delta",
            title = {'text': "Radiación (W/m2)"},
            delta = {'reference': 1300},
            gauge = {'axis': {'range': [None, 2000]},
                    'steps' : [
                        {'range': [0, 1000], 'color': "beige"},
                        {'range': [1000, 1600], 'color': "lime"},
                        {'range': [1600, 2000], 'color': "orangered"}]}))

    
    
    plot_div_temp = plot({'data': fig_temp}, output_type='div')
    plot_div_prec = plot({'data': fig_prec}, output_type='div')
    plot_div_rad = plot({'data': fig_rad}, output_type='div')

    cotx={'plot_div_temp': plot_div_temp, 'plot_div_prec': plot_div_prec, 'plot_div_rad': plot_div_rad}

    return render(request, 'gauges_views.html', context=cotx)