from django.shortcuts import render,reverse
from.forms import FormularioErgometria
from core.models import Pacientes
from.models import Ergometria
from django.views.generic import ListView,UpdateView,DeleteView
# Create your views here.

def cargaErgo(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        eventos = Pacientes.objects.filter(nombre__icontains=q)
        return render(request, 'ergo/ergometria.html', {'eventos': eventos})
    if request.method == 'POST':
        form=FormularioErgometria(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid():
             #pregunto si mis datos son validos
            form.save(commit=True) #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=FormularioErgometria()#caso contrario atualizo la misma pagina del forulario
        return render(request,'ergo/ergometria.html')#renerizo indicando que exitste formulario
    return render(request,"'ergo/ergometria.html",{'form':form})


def Lista_ergo(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        eventos = Ergometria.objects.filter(id_ergo__icontains=q)
        return render(request, 'ergo/listaergometria.html', {'eventos': eventos})

class Edita_ergo(UpdateView):
    model=Ergometria
    form_class=FormularioErgometria
    template_name='ergo/editaergo.html'
    def get_success_url(self):
        return reverse('listaergo')
class Borra_ergo(DeleteView):
    model=Ergometria
    template_name='ergo/borraergo.html'
    def get_success_url(self):
        return reverse('listaergo')
