from django.shortcuts import render


def inicio(request):
    context = {
        "nombre": "pepe"
    }
    return render(request, "inicio.html", context=context)