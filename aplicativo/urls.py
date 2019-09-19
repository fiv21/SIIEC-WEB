from django.urls import path
from.import views
#aca genero las urls que va a tener la app core de nuestro proyecto 
urlpatterns = [

    #path de aplicativo
    path('aplicativo/', views.aplicativo, name="aplicativo"),
    path('preinforme/', views.preinforme, name="preinforme"),
    
    
]