# Generated by Django 2.0.10 on 2019-03-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='complain_base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=15)),
                ('kode_toko', models.CharField(max_length=4)),
                ('nama_toko', models.CharField(max_length=50)),
                ('sid', models.IntegerField()),
                ('ip_public', models.CharField(max_length=15)),
            ],
        ),
    ]