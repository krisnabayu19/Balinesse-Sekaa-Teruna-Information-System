from django import forms
from .models import UserModel, TentangCompanyModel, VisiCompanyModel, KegiatanCompanyModel, PengurusCompanyModel, NarahubungCompanyModel, EmailModelCompany, BeritaModel, BeritaEditModel, BeritaCommentModel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"

class TentangForm(forms.ModelForm):
    class Meta:
        model = TentangCompanyModel
        fields = "__all__"

class VisiForm(forms.ModelForm):
    class Meta:
        model = VisiCompanyModel
        fields = "__all__"

class KegiatanForm(forms.ModelForm):
    class Meta:
        model = KegiatanCompanyModel
        fields = "__all__"

class PengurusForm(forms.ModelForm):
    class Meta:
        model = PengurusCompanyModel
        fields = "__all__"

class NarahubungForm(forms.ModelForm):
    class Meta:
        model = NarahubungCompanyModel
        fields = "__all__"

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailModelCompany
        fields = "__all__"

class BeritaForm(forms.ModelForm):
    class Meta:
        model = BeritaModel
        fields = ['count_comment']

class UploadBeritaForm(forms.ModelForm):
    class Meta:
        model = BeritaModel
        fields = "__all__"

class BeritaEditForm(forms.ModelForm):
    class Meta:
        model = BeritaEditModel
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = BeritaCommentModel
        fields = "__all__"