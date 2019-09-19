from django.shortcuts import render


def aplicativo(request):
    return render(request, "aplicativo/aplicativo.html")
# Create your views here.
def preinforme(request):
    return render(request,"aplicativo/Vista.html")