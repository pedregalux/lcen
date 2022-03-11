from django import forms

# Create your forms here.


class GlosarioForm(forms.Form):
    palabra = forms.CharField(label='Your name', max_length=100)
