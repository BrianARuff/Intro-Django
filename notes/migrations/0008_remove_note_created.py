# Generated by Django 2.1.4 on 2018-12-03 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20181203_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='created',
        ),
    ]
