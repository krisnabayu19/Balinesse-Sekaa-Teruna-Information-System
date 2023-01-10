# Generated by Django 4.1.1 on 2022-10-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('is_superuser', models.IntegerField(blank=True, null=True)),
                ('is_staff', models.IntegerField(blank=True, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('verified', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
    ]
