from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


#Create a registration form
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input is-medium is-rounded', 'placeholder' : 'Email'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input is-medium is-rounded', 'placeholder' : 'First Name' }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input is-medium is-rounded', 'placeholder' : 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input is-medium is-rounded'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        
        self.fields['password1'].widget.attrs['class'] = 'input is-medium is-rounded'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['password2'].widget.attrs['class'] = 'input is-medium is-rounded'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password'
