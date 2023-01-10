from django.db import models

# Create your models here.
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

class AwigModel(models.Model):
    id_awigawig = models.AutoField(primary_key=True)
    nama_awigawig = models.CharField(max_length=200, blank=True, null=True)
    deskripsi_awigawig = models.CharField(max_length=200, blank=True, null=True)
    awigawig_path = models.FileField(upload_to='awigawig/', null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    id_user_created = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_awigawig'
