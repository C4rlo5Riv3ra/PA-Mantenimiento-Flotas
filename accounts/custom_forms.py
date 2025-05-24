
from allauth.account.forms import SignupForm  
from django import forms
from proyect.choices import rol

class CustomSignupForm(SignupForm  ):
    id_rol = forms.ChoiceField(choices=rol, label="rol", required=True)

    def save(self, request):
        user = super().save(request)
        user.id_rol = self.cleaned_data['id_rol']
        user.save()
        return user
