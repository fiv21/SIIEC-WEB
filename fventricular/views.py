from django.shortcuts import render,reverse
from.forms import ventricularFormu
from core.models import Pacientes
from core.models import Estudio
from.models import FuncionVentricular
from django.views.generic import ListView,UpdateView,DeleteView
# Create your views here.

def formventricular(request):
 
    
    if request.method == 'GET':
        q = request.GET.get('q', '')
        eventos = Estudio.objects.filter(pacientes__dni__icontains=q)
        #estudios=Estudio.objects.all()
        return render(request, 'fventricular/fventricular.html', {'eventos': eventos}) #'estudios': estudios}

    if request.method == 'POST':
        form=ventricularFormu(request.POST) #indico metodos POST de la transmicion de mis datos
        if form.is_valid(): #pregunto si mis datos son validos
            form.save() #guardo
        return render(request,"core/home.html")#al ser esto exitoso redirecciono a home
    else:
        form=ventricularFormu()#caso contrario atualizo la misma pagina del forulario
    return render(request,"fventricular/fventricular.html",{'form':form})

def Lista_ventricular(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        eventos = FuncionVentricular.objects.filter(paciente_fv__dni__icontains=q)
        return render(request, 'fventricular/listaventricular.html', {'eventos': eventos})

class Edita_ventricular(UpdateView):
    model=FuncionVentricular
    form_class=ventricularFormu
    template_name='fventricular/editaventricular.html'
    def get_success_url(self):
        return reverse('listaventricular')
class Borra_ventricular(DeleteView):
    model=FuncionVentricular
    template_name='fventricular/borraventricular.html'
    def get_success_url(self):
        return reverse('listaventricular')