# Generated by Django 3.2.8 on 2021-11-02 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'задача', 'verbose_name_plural': 'задачи'},
        ),
    ]
