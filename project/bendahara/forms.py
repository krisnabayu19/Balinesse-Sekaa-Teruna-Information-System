from django import forms
from .models import IuranModel, UpdateIuranModel, KeuanganModel, UserProfileModel

class IuranForm(forms.ModelForm):
    class Meta:
        model = IuranModel
        fields = "__all__"

class IuranUpdateForm(forms.ModelForm):
    class Meta:
        model = UpdateIuranModel
        fields = "__all__"

class KeuanganForm(forms.ModelForm):
    class Meta:
        model = KeuanganModel
        fields = ['id_keuangan','nama_keuangan','tipe_keuangan','id_jenis_agenda','jumlah_keuangan','deskripsi_keuangan','tanggal_keuangan','file_path']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['id','full_name','first_name','last_name','email','image']