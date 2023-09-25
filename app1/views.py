from django.shortcuts import render
from django.http import HttpResponse



def vista1(request):
    return HttpResponse ("<h1>Primera vista de la primera app</h1>"
                         "<h2> francisco muñoz </h2> "
                         "<h3> 25-09-2023 </h3>"
                         "<h3>certamen 1</h3>"
                         )



