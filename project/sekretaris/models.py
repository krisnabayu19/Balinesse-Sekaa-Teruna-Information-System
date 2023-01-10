from django.db import models
from authentification.models import UserModel
from bendahara.models import IuranModel

# Create your models here.
class JenisAgendaModel(models.Model):
    id_jenis_agenda = models.AutoField(primary_key=True)
    nama_jenis_agenda = models.CharField(max_length=200, blank=True, null=True)
    id_user_created = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_jenis_agenda'

class AgendaModel(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    nama_agenda = models.CharField(max_length=200, blank=True, null=True)
    id_jenis_agenda = models.ForeignKey(JenisAgendaModel, models.DO_NOTHING, db_column='id_jenis_agenda')
    deskripsi_agenda = models.TextField(blank=True, null=True)
    id_iuran = models.ForeignKey(IuranModel, models.DO_NOTHING, db_column='id_iuran')
    tanggal_agenda = models.DateTimeField(blank=True, null=True)
    hasil_agenda = models.CharField(max_length=200, blank=True, null=True)
    id_user_created = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agenda'

class LpjModel(models.Model):
    id_lpj = models.AutoField(primary_key=True)
    nama_lpj = models.CharField(max_length=200, blank=True, null=True)
    deskripsi_lpj = models.TextField(blank=True, null=True)
    tanggal_lpj = models.DateTimeField(blank=True, null=True)
    file_path = models.FileField(upload_to='lpj/',null=True, blank=True)
    id_user_created = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_lpj'

class AbsensiModel(models.Model):
    id_absensi = models.AutoField(primary_key=True)
    id_agenda = models.ForeignKey(AgendaModel, models.DO_NOTHING, db_column='id_agenda')
    id_user = models.ForeignKey(UserModel, models.DO_NOTHING, db_column='id_user')
    status_absensi = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'tb_absensi'

class AbsensiGenerateModel(models.Model):
    id_absensi = models.AutoField(primary_key=True)
    id_agenda = models.IntegerField(blank=True, null=True)
    id_user = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'tb_absensi'

class UpdateAbsensiModel(models.Model):
    id_absensi = models.AutoField(primary_key=True)
    status_absensi = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_absensi'

class UserRekapAbsensi(models.Model):
    id_user_rekap = models.AutoField(primary_key=True)
    tanggal_agenda = models.DateTimeField(blank=True, null=True)
    nama_agenda = models.CharField(max_length=200, blank=True, null=True)
    status_absensi = models.IntegerField(blank=True, null=True)

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



