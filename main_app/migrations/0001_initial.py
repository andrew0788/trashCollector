# Generated by Django 2.2.2 on 2019-06-11 03:29

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', django_google_maps.fields.AddressField(max_length=200)),
                ('description', models.TextField(max_length=250)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]