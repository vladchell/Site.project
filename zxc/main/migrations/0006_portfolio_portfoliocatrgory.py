# Generated by Django 3.2.8 on 2021-11-18 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_mymodel_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCatrgory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('image', models.ImageField(upload_to='image')),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.portfoliocatrgory')),
            ],
        ),
    ]
