# Generated by Django 3.1.1 on 2021-02-05 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userImage', models.ImageField(blank=True, default='default/default.png', upload_to='Store')),
                ('store_name', models.CharField(max_length=300)),
                ('address1', models.TextField()),
                ('locality', models.TextField()),
                ('city', models.CharField(max_length=300)),
                ('pincode', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(max_length=300)),
                ('contact', models.CharField(blank=True, max_length=300)),
                ('openingtime', models.TimeField(blank=True)),
                ('closingtime', models.TimeField(blank=True)),
                ('limit', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('store_email', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('limit', models.IntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.store')),
            ],
        ),
    ]