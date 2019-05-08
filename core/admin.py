from django.contrib import admin
from.models import Paciente
# Register your models here.
class PorjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Paciente) #asi hago visible la base de datos de esta app en el sitio administrador de django.