# Generated by Django 2.1.4 on 2018-12-03 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20181203_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created',
            field=models.DateTimeField(default='2018-12-03T23:02:04.076082'),
        ),
    ]
