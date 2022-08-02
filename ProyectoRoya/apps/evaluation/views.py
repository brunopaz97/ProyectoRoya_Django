from django.shortcuts import render

# Create your views here.

def ingresardatos(request):
	return render(request, 'formulario_ingreso_datos.html')


