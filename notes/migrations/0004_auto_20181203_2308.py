# Generated by Django 2.1.4 on 2018-12-03 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(default='2018-12-03T23:08:58.557224', editable=False),
        ),
    ]
