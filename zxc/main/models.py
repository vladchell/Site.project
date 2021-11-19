from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.CharField('Name',max_length=20)
    email = models.EmailField('Email')
    phonenumber = PhoneNumberField('Phone')
    message = models.TextField('Message')

    def __str__(self):
        return self.name

class PortfolioCatrgory(models.Model):
    name = models.CharField('name',max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField('name', max_length=20)
    image = models.ImageField(upload_to='static/image')
    category = models.ForeignKey('PortfolioCatrgory',on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.name