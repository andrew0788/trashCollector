# Generated by Django 2.2.2 on 2019-06-16 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20190616_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seen',
            options={'ordering': ['-time_seen']},
        ),
    ]