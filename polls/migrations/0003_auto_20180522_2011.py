# Generated by Django 2.0.5 on 2018-05-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_dane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dane',
            name='zysk_netto',
            field=models.IntegerField(default=0),
        ),
    ]