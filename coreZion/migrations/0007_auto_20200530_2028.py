# Generated by Django 3.0.6 on 2020-05-31 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreZion', '0006_auto_20200530_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atleta',
            name='nome',
            field=models.CharField(max_length=11, verbose_name='Nome'),
        ),
    ]
