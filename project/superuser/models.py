from xmlrpc.client import boolean
from django.db import models


# Create your models here.
class UserModel(models.Model):
    a = boolean
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'

class TentangCompanyModel(models.Model):
    id_tentang_company = models.AutoField(primary_key=True)
    deskripsi_tentang_company = models.TextField( blank=True, null=True)
    image_tentang_company = models.ImageField(upload_to='tentang/', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_tentang_company'

class VisiCompanyModel(models.Model):
    id_visi_company = models.AutoField(primary_key=True)
    title_visi_company = models.TextField( blank=True, null=True)
    deskripsi_visi_company = models.TextField( blank=True, null=True)
    image_visi_company = models.ImageField(upload_to='visi/', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_visi_company'

class KegiatanCompanyModel(models.Model):
    id_kegiatan_company = models.AutoField(primary_key=True)
    title_kegiatan_company = models.TextField( blank=True, null=True)
    deskripsi_kegiatan_company = models.TextField( blank=True, null=True)
    image_kegiatan_company = models.ImageField(upload_to='kegiatan/', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_kegiatan_company'

class PengurusCompanyModel(models.Model):
    id_pengurus_company = models.AutoField(primary_key=True)
    nama_pengurus_company = models.TextField( blank=True, null=True)
    jabatan_pengurus_company = models.TextField( blank=True, null=True)
    image_pengurus_company = models.ImageField(upload_to='pengurus/', null=True, blank=True)
    periode_mulai_company = models.DateField( blank=True, null=True)
    periode_berakhir_company = models.DateField( blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_pengurus_company'

class BeritaModel(models.Model):
    id_berita = models.AutoField(primary_key=True)
    date_berita = models.DateTimeField( blank=True, null=True)
    judul_berita = models.TextField( blank=True, null=True)
    deskripsi_berita = models.TextField( blank=True, null=True)
    image_berita = models.ImageField(upload_to='berita/', null=True, blank=True)
    count_comment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_berita'

class BeritaEditModel(models.Model):
    id_berita = models.AutoField(primary_key=True)
    date_berita = models.DateTimeField( blank=True, null=True)
    judul_berita = models.TextField( blank=True, null=True)
    deskripsi_berita = models.TextField( blank=True, null=True)
    image_berita = models.ImageField(upload_to='berita/', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_berita'

class CommentEditModel(models.Model):
    id_berita = models.AutoField(primary_key=True)
    count_comment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_berita'

class NarahubungCompanyModel(models.Model):
    id_narahubung = models.AutoField(primary_key=True)
    address_narahubung = models.TextField( blank=True, null=True)
    phonenumber_narahubung = models.TextField( blank=True, null=True)
    email_narahubung = models.TextField( blank=True, null=True)
    clock_narahubung = models.TextField( blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_narahubung'

class EmailModelCompany(models.Model):
    id_email_company = models.AutoField(primary_key=True)
    name_sender_company = models.TextField(blank=True, null=True)
    email_address_sender_company = models.TextField(blank=True, null=True)
    subject_email_sender_company = models.TextField(blank=True, null=True)
    message_email_sender_company = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_email_company'

class BeritaCommentModel(models.Model):
    id_comment = models.AutoField(primary_key=True)
    id_berita = models.IntegerField(blank=True, null=True)
    name_sender = models.TextField(blank=True, null=True)
    email_address_sender = models.TextField(blank=True, null=True)
    berita_comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField( blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_berita_comment'


