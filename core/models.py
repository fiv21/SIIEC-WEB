from django.db import models

# Create your models here.
#generando los modelos que van a contener la tabla de la base de datos
class Paciente (models.Model):
    estudio=models.CharField(max_length=50,verbose_name="Estudio")
    fechaAcutal=models.DateTimeField(auto_now_add=True,verbose_name="Fecha Actual")
    apellidoNombre=models.CharField(max_length=50,verbose_name="Apellido y Nombre")
    dni=models.IntegerField(verbose_name="Dni")
    coberturaMedica=models.CharField(max_length=50,verbose_name="Cobertura Medica")
    sexo=models.CharField(max_length=20,verbose_name="Sexo")
    medico=models.CharField(max_length=50,verbose_name="Medico")
    peso=models.FloatField(verbose_name="Peso")
    talla=models.FloatField(verbose_name="Talla")
    indicacion=models.CharField(max_length=50,verbose_name="Indicacion")
    decubito=models.CharField(max_length=50,verbose_name="Decubito")
    perimetroAbdominal=models.IntegerField(verbose_name="Perimetro Abdominal")
    edad=models.IntegerField(verbose_name="Edad")
    fechaNacimiento=models.DateField(verbose_name="Fecha de nacimiento")
    imc=models.IntegerField(verbose_name="Imc")
    supCorporal=models.FloatField(verbose_name="Superficie corporal")
    calidadTecnica=models.IntegerField(verbose_name="Calidad tecnica")
    observaciones=models.TextField(verbose_name="Observaciones")
class Meta: #aplicando un metodo para que pase a español en el admin del framework
        verbose_name= "Paciente"#aca los paso al español en singular
        verbose_name_plural="Pacientes"#aca los paso al español en prural
        ordering = ["created"] #con esta funcion puedo ordenar los objetos a medida que los creo


