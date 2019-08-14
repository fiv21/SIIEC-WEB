from django.shortcuts import render,reverse
from.forms import formAntecedentes
from django.db.models import Q
from core.models import Pacientes
from.models import Antecedentes
from django.views.generic import ListView,UpdateView,DeleteView
# Create your views here.

def form_antecedente(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        eventos = Pacientes.objects.filter(nombre__icontains=q)
        return render(request, 'antec/antecedentes.html', {'eventos': eventos})

    if request.method == 'POST':
        form=formAntecedentes(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid():
             #pregunto si mis datos son validos
            form.save(commit=True) #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=formAntecedentes#caso contrario atualizo la misma pagina del forulario
        return render(request,'antec/antecedentes.html')#renerizo indicando que exitste formulario
    return render(request,"antec/antecedentes.html",{'form':form})

def Lista_antecedentes(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        eventos = Antecedentes.objects.filter(id_antecedentes__icontains=q)
        return render(request, 'antec/listaantecedentes.html', {'eventos': eventos})

class Edita_antecedentes(UpdateView):
    model=Antecedentes
    form_class=formAntecedentes
    template_name='antec/editaantecedentes.html'
    def get_success_url(self):
        return reverse('listaantecedentes')
class Borra_antecedente(DeleteView):
    model=Antecedentes
    template_name='antec/borraantecedentes.html'
    def get_success_url(self):
        return reverse('listaantecedentes')
