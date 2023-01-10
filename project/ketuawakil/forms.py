from django import forms
from .models import UserProfileModel, AwigModel

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['id','full_name','first_name','last_name','email','image']

class AwigForm(forms.ModelForm):
    class Meta:
        model = AwigModel
        fields = ['id_awigawig','nama_awigawig','deskripsi_awigawig','awigawig_path','created_at','id_user_created']

