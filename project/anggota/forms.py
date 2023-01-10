from django import forms
from .models import UserProfileModel

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['id','full_name','first_name','last_name','email','image']
