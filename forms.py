from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User , Group
from django import forms
from django.forms.widgets import PasswordInput , TextInput
from .models import Image , Video , Audio , Msg , Song , Latest , Hollywood , Bollywood , Engweb , Hindiweb , South


admin.site.unregister(Group)



class MsgForm(forms.ModelForm):
    body = forms.CharField(required=True , widget=forms.widgets.Textarea(
         attrs={'placeholder': 'Write Msg....' , 'class':'form-control' }),
         label="")
    
    class Meta:
        model = Msg
        exclude = ('user',)


class Register_form(UserCreationForm):
    class Meta:
         
         model = User
         fields = ['username' , 'email' , 'password1' , 'password2']


class Login_form(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class ImageForm(forms.ModelForm):
     class Meta:
        model=Image
        fields=("caption","image")


class Video_form(forms.ModelForm):
    class Meta:
     model=Video
     fields=("caption","video")

class Audio_form(forms.ModelForm):
    class Meta:
     model=Audio
     fields=("caption","audio")


class Song_form(forms.ModelForm):
    class Meta:
     model=Song
     fields=("caption","song")

    

class Lastest_form(forms.ModelForm):
    class Meta:
     model=Latest
     fields=("caption","video")


class Hollywood_form(forms.ModelForm):
    class Meta:
     model=Hollywood
     fields=("caption","video")



class Bollywood_form(forms.ModelForm):
    class Meta:
     model=Bollywood
     fields=("caption","video")



class South_form(forms.ModelForm):
    class Meta:
     model=South
     fields=("caption","video")




class Engweb_form(forms.ModelForm):
    class Meta:
     model=Engweb
     fields=("caption","video")



class Hindiweb_form(forms.ModelForm):
    class Meta:
     model=Hindiweb
     fields=("caption","video")



