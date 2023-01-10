from django import forms

from anggota.models import UserProfileModel
from .models import AgendaModel, LpjModel, UpdateAbsensiModel, JenisAgendaModel, UserProfileModel

class JenisAgendaForm(forms.ModelForm):
    class Meta:
        model = JenisAgendaModel
        fields = "__all__"

class AgendaForm(forms.ModelForm):
    class Meta:
        model = AgendaModel
        fields = "__all__"

class LpjForm(forms.ModelForm):
    class Meta:
        model = LpjModel
        fields = ['id_lpj','nama_lpj','deskripsi_lpj','tanggal_lpj','file_path']

class AbsensiForm(forms.ModelForm):
    class Meta:
        model = UpdateAbsensiModel
        fields = "__all__"

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['id','full_name','first_name','last_name','email','image']
