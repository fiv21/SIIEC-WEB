from django.urls import path
from.import views
#aca genero las urls que va a tener la app core de nuestro proyecto 
urlpatterns = [

    #path del core
    path('', views.home, name="home"),
    path('formpaciente/', views.fomPaciente, name="form"),
    path('cargapaciente/', views.cargaPacientes, name="pacienteform"),
    
    
]