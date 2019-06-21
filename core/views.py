from django.shortcuts import render
from.forms import estudioFormu
# Create your views here
#en esta parte se generan las vistas para direccionar nuestra app 
def fomPaciente(request):
    if request.method == 'POST':
        form=estudioFormu(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid(): #pregunto si mis datos son validos
            form.save() #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=estudioFormu()#caso contrario atualizo la misma pagina del forulario
    return render(request,"core/formPaciente.html",{'form':form}) #renerizo indicando que exitste formulario
def home(request):
    return render(request,"core/home.html",context=None) #funcion de la vista home 


