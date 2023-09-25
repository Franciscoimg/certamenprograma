from django.shortcuts import render
from django.http import HttpResponse 

def vista1(request):
    return HttpResponse ("<h1>Esta es una etiqueta H1. Utilízala en el título.</h1>"
                        "<h2>Esta es una etiqueta H2. Utilízala en los encabezados de secciones.</h2>"
                        "<h3>Esta es una etiqueta H3. Utilízala en sub-secciones.</h3>"

                                    )

def vista2(request):
    return HttpResponse ("<h1>godoy</h1>"
                        "<h2>muñoz.</h2>"
                        "<h3>francisco.</h3>"

                                    )
