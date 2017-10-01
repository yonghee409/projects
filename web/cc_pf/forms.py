from django.forms import ModelForm
from .models import ApiKeyset
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Form_ApiKeyset(ModelForm):
    class Meta:
        model = ApiKeyset
        fields = ['alias','apikey','apisecret']

class Form_Signup(UserCreationForm):
    email = forms.EmailField(
        require=True,
        widget=forms.EmailInput(
            attr={
                'class':'form-control',
                'placeholder':'Email',
                'required':'True'
            }
        )
    )
    class Meta:
        model = User;
        fields = ["email","password1","password2"]
