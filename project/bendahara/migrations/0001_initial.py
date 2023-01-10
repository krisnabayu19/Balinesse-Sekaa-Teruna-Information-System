# Generated by Django 4.1.1 on 2022-10-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaModel1',
            fields=[
                ('id_agenda', models.AutoField(primary_key=True, serialize=False)),
                ('nama_agenda', models.CharField(blank=True, max_length=200, null=True)),
                ('id_jenis_agenda', models.CharField(blank=True, max_length=200, null=True)),
                ('deskripsi_agenda', models.TextField(blank=True, null=True)),
                ('tanggal_agenda', models.DateTimeField(blank=True, null=True)),
                ('hasil_agenda', models.CharField(blank=True, max_length=200, null=True)),
                ('id_user_created', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_agenda',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IuranGenerateModel',
            fields=[
                ('id_iuran_rekap', models.AutoField(primary_key=True, serialize=False)),
                ('id_agenda', models.IntegerField(blank=True, null=True)),
                ('id_user', models.IntegerField(blank=True, null=True)),
                ('iuran', models.IntegerField(blank=True, null=True)),
                ('total_iuran', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_iuran_rekap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IuranModel',
            fields=[
                ('id_iuran', models.AutoField(primary_key=True, serialize=False)),
                ('jumlah_iuran', models.IntegerField(blank=True, null=True)),
                ('id_user_created', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_iuran',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IuranRekapModel',
            fields=[
                ('id_iuran_rekap', models.AutoField(primary_key=True, serialize=False)),
                ('iuran', models.IntegerField(blank=True, null=True)),
                ('status_iuran', models.IntegerField(blank=True, null=True)),
                ('total_iuran', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_iuran_rekap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JenisAgendaModel',
            fields=[
                ('id_jenis_agenda', models.AutoField(primary_key=True, serialize=False)),
                ('nama_jenis_agenda', models.CharField(blank=True, max_length=200, null=True)),
                ('id_user_created', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_jenis_agenda',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KeuanganModel',
            fields=[
                ('id_keuangan', models.AutoField(primary_key=True, serialize=False)),
                ('nama_keuangan', models.CharField(blank=True, max_length=200, null=True)),
                ('tipe_keuangan', models.CharField(blank=True, max_length=200, null=True)),
                ('jumlah_keuangan', models.IntegerField(blank=True, null=True)),
                ('deskripsi_keuangan', models.TextField(blank=True, null=True)),
                ('id_user_created', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_keuangan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UpdateIuranModel',
            fields=[
                ('id_iuran_rekap', models.AutoField(primary_key=True, serialize=False)),
                ('status_iuran', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_iuran_rekap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
    ]
