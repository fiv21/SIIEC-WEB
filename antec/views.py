from django.shortcuts import render
from.forms import formAntecedentes

# Create your views here.

def form_antecedente(request):
    
    if request.method == 'POST':
        form=formAntecedentes(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid():
             #pregunto si mis datos son validos
            form.save(commit=True) #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=formAntecedentes#caso contrario atualizo la misma pagina del forulario
    return render(request,"antec/antecedentes.html",{'form':form}) #renerizo indicando que exitste formulario


