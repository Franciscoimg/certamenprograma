from django.shortcuts import render
from django.http import HttpResponse

def vista1(request):
    return HttpResponse ("<h1> hola como estamos </h1>"
                        "<h2>francisco muñoz  </h2>"
                         
                         
                         )

def vista2(request):
    return HttpResponse ("<h1>certmen 1</h1>"
                         "<h2>viva chile </h2>"
            
                         )
