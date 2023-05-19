from django import forms
from django.db import transaction
from django.forms import ModelForm
from propuestas.models import Propuesta, TemaPropuesta, SubtemaPropuesta
from usuarios.models import Organizacion
from mantenedores.models import *



class PropuestaForm1(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'pais',
        'region',
        'comuna'
        ]
        labels = {
            'pais': ('1. País -- Selecciona el país desde donde ingresas la propuesta'),
            'region': ('2. Región -- Selecciona la región relacionada con la propuesta, si corresponde'),
            'comuna': ('3. Comuna -- Selecciona la comuna relacionada con la propuesta, si corresponde'),
        }



class PropuestaForm2(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'tema',
        'otros_temas',
        'tema_extra',
        ]
        labels = {
            'tema': ('1. ¿Cuál es el tema principal de tu propuesta? -- Selecciona el tema principal desde la lista desplegable'),
            'otros_temas': ('2. ¿Qué otros temas aborda tu propuesta? -- Por favor selecciona hasta tres temas adicionales, debes seleccionarlos con el mouse y apretando la telca Control -Ctrl-'),
            'tema_extra': ('3. Otro tema, ¿cuál? -- Si tu propuesta contempla algún tema que no está en el listado, por favor escríbelo aquí en una palabra o frase breve -máximo 100 cars.-'),
        }



class PropuestaForm3(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'problema',
        'situacion',
        'componente'
        ]
        labels = {
            'problema': ('1. ¿Cuál es el problema que tú o tu organización busca solucionar? -- Ejemplo: El actual sistema de seguridad social no garantiza pensiones dignas para todas las personas.'),
            'situacion': ('2. Con respecto al problema planteado, ¿cuál sería la situación ideal? -- Ejemplo: Cuando jubilan, todas las personas tienen acceso a una pensión que cubre sus necesidades básicas para vivir con dignidad.'),
            'componente': ('3. Para avanzar en el logro de esa situación ideal, ¿qué debería contemplar la Nueva Constitución? -- Ejemplo: Consagrar constitucionalmente el derecho a la protección social y explicitar la obligación del Estado de asegurar a todas las personas una pensión digna.'),
        }
        widgets = {
            'problema': forms.Textarea(attrs={'placeholder': 'Describe el problema de manera precisa y breve en un máximo de 250 palabras.'}),
            'situacion': forms.Textarea(attrs={'placeholder': 'Describe la situación ideal de manera precisa y breve en un máximo de 250 palabras.'}),
            'componente': forms.Textarea(attrs={'placeholder': 'Escribe tu propuesta de manera precisa y breve en un máximo de 250 palabras.'}),
        }



class PropuestaForm4(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'otras_organizaciones',
        'organizaciones_de_propuesta',
        'organizaciones',
        ]
        widgets = {
            'otras_organizaciones': forms.CheckboxInput()
        }
        labels = {
            'otras_organizaciones': ('1. ¿Esta propuesta fue elaborada en conjunto con otras organizaciones? -- Marque si es así.'),
            'organizaciones_de_propuesta': ('2. Si tu respuesta fue “sí”, escribe cuáles: -- Por favor escribe los nombres de las organizaciones que participaron en la elaboración de la propuesta, separados por comas ¡No olvides incluir a tu organización!'),
            'organizaciones': ('Sólo si eres una Organización: ¿Esta Propuesta involucra a otras organizaciones que están en La Constitución es Nuestra? Ten en cuenta que la cocreación de propuestas debe ser oficial, sino la propuesta será corregida -- Si la organización de la que formas parte está en La Constitución es Nuestra, debes ingresar la propuesta a través del perfil de la organización y no como un usuarix particular. Si eres una organización y quieres incluir en la creación de la propuesta a organizaciones adicionales, debes seleccionarlas con el mouse y apretando la telca Control -Ctrl-'),
        }



class PropuestaForm4a(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'otras_organizaciones',
        'organizaciones_de_propuesta',
        ]
        widgets = {
            'otras_organizaciones': forms.CheckboxInput()
        }
        labels = {
            'otras_organizaciones': ('1. ¿Esta propuesta fue elaborada en conjunto con otras organizaciones? -- Marque si es así.'),
            'organizaciones_de_propuesta': ('2. Si tu respuesta fue “sí”, escribe cuáles: -- Por favor escribe los nombres de las organizaciones que participaron en la elaboración de la propuesta, separados por comas ¡No olvides incluir a tu organización!'),
        }



class PropuestaForm5(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'compromiso_convencionales',
        'anexo3_propuesta',
        ]
        widgets = {
            'compromiso_convencionales': forms.CheckboxInput()
        }
        labels = {
            'compromiso_convencionales': ('1. ¿Tu propuesta cuenta con compromisos formales de apoyo de convencionales constituyentes? -- Marque si es así.'),
            'anexo3_propuesta': ('Si tienes un documento o archivo que acredite los compromisos, ingrésalo acá. Por favor no subir documentos con peso mayor a 10MB.'),
        }



class PropuestaForm6(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'anexo_propuesta',
        'anexo2_propuesta',
        'link_extra1',
        'link_extra2'
        ]
        labels = {
            'anexo_propuesta': ('Si has elaborado un documento con tu propuesta constitucional desarrollada en mayor detalle y profundidad, adjúntalo -no subir documentos con peso mayor a 10MB-:</span></h6>'),
            'anexo2_propuesta': ('Asimismo, si cuentas con otros materiales que complementen tu propuesta (estudios, encuestas, presentaciones, material comunicacional, etc.) , agrégalos acá. No subir documentos con peso mayor a 10MB.'),
            'link_extra1': ('Si hay una página o documento online, ingresa un link a material complementario.'),
            'link_extra2': ('Otro link a material complementario.'),
        }



class PropuestaForm7(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = [
        'titulo'
        ]
        labels = {
            'titulo': ('Escribe un título atractivo para que podamos difundirla entre la ciudadanía y en la Convención Constitucional. -- Título: máximo 280 caracteres.'),
        }



# class CrearPropuestaForm(forms.ModelForm):
#     class Meta:
#         model = Propuesta
#         fields = [
#         'pais',
#         'region',
#         'comuna',
#         'tema',
#         'otros_temas',
#         'problema',
#         'situacion',
#         'componente',
#         'otras_organizaciones',
#         'organizaciones_de_propuesta',
#         'compromiso_convencionales',
#         'convencionales_comprometidos',
#         'anexo_propuesta',
#         'titulo'
#         ]
