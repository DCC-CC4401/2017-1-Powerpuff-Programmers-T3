from django import forms

class SignUp(forms.Form):
    tipos = (('Alumno', 'Alumno'), ('Fijo', 'Vendedor Fijo'), ('Ambulante', 'Vendedor Ambulante'), ('Admin', 'Administrador'))
    tipo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'multiple'}), choices=tipos, required=False)
    username = forms.CharField(max_length=60, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)