from django import forms
from.models import Paciente
#en esta parte se genera el back end de los formularios web 
#generando otra forma de cargar los datos desde la pagina web

class pacienteFormu(forms.ModelForm):
    class Meta:
        model=Paciente # aca indicamos los campos que vamos a utilizar 

        fields= [
            'estudio',
            'fechaNacimiento',
            'apellidoNombre',
            'dni',
            'coberturaMedica',
            'sexo',
            'medico',
            'peso',
            'talla',
            'indicacion',
            'decubito',
            'perimetroAbdominal',
            'edad',
            'imc',
            'supCorporal',
            'calidadTecnica',
            'observaciones',
        ]
        labels = {
            'estudio' : 'Estudio',
            'apellidoNombre' : 'Apellido y Nombre',
            'dni' : 'Dni',
            'coberturaMedica' : 'Cobertura medica',
            'sexo' : 'Sexo',
            'medico' : 'Medico',
            'peso' : 'Peso',
            'talla' : 'Talla',
            'indicacion' : 'Indicacion',
            'decubito' : 'Decubito',
            'perimetroAbdominal' : 'Perimetro abdominal',
            'edad': 'Edad',
            'fechaNacimiento' : 'Fecha de nacimiento',
            'imc' : 'Imc',
            'supCorporal' : 'Superficie corporal',
            'calidadTecnica' : 'Calidad tecnica',
            'observaciones' : 'Observaciones',
        }

        


        

        




