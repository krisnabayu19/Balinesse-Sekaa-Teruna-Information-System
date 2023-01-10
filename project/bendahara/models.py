from django.db import models
from authentification.models import UserModel

# Create your models here.


class IuranModel(models.Model):
    id_iuran = models.AutoField(primary_key=True)
    jumlah_iuran = models.IntegerField(blank=True, null=True)
    id_user_created = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_iuran'

class AgendaModel1(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    nama_agenda = models.CharField(max_length=200, blank=True, null=True)
    id_jenis_agenda = models.CharField(max_length=200, blank=True, null=True)
    deskripsi_agenda = models.TextField(blank=True, null=True)
    id_iuran = models.ForeignKey(IuranModel, models.DO_NOTHING, db_column='id_iuran')
    tanggal_agenda = models.DateTimeField(blank=True, null=True)
    hasil_agenda = models.CharField(max_length=200, blank=True, null=True)
    id_user_created = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda'

class IuranRekapModel(models.Model):
    id_iuran_rekap = models.AutoField(primary_key=True)
    id_agenda = models.ForeignKey(AgendaModel1, models.DO_NOTHING, db_column='id_agenda')
    id_user = models.ForeignKey(UserModel, models.DO_NOTHING, db_column='id_user')
    iuran = models.IntegerField(blank=True, null=True)
    status_iuran = models.IntegerField(blank=True, null=True)
    total_iuran = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_iuran_rekap'

class IuranGenerateModel(models.Model):
    id_iuran_rekap = models.AutoField(primary_key=True)
    id_agenda = models.IntegerField(blank=True, null=True)
    id_user = models.IntegerField(blank=True, null=True)
    iuran = models.IntegerField(blank=True, null=True)
    total_iuran = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_iuran_rekap'

class UpdateIuranModel(models.Model):
    id_iuran_rekap = models.AutoField(primary_key=True)
    status_iuran = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_iuran_rekap'

class JenisAgendaModel(models.Model):
    id_jenis_agenda = models.AutoField(primary_key=True)
    nama_jenis_agenda = models.CharField(max_length=200, blank=True, null=True)
    id_user_created = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_jenis_agenda'

class KeuanganModel(models.Model):
    id_keuangan = models.AutoField(primary_key=True)
    nama_keuangan = models.CharField(max_length=200, blank=True, null=True)
    tipe_keuangan = models.CharField(max_length=200, blank=True, null=True)
    id_jenis_agenda = models.ForeignKey(JenisAgendaModel, models.DO_NOTHING, db_column='id_jenis_agenda')
    jumlah_keuangan = models.IntegerField(blank=True, null=True)
    deskripsi_keuangan = models.TextField(blank=True, null=True)
    tanggal_keuangan = models.DateTimeField(blank=True, null=True)
    file_path = models.FileField(upload_to='keuangan/',null=True, blank=True)
    id_user_created = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_keuangan'

class UserProfileModel(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'auth_user'
    
