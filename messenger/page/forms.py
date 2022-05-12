from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = {'avatar', 'sex'}

class ChatEdit(ModelForm):
    class Meta:
        model = Chat
        fields = {'penPal', 'nameChat',}