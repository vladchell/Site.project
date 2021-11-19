from django import forms
from .models import Contact
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(
                attrs={
                      #< input type = "text"class ="form-control" placeholder="Name" >
                    'class':'form-control',
                    'placeholder':'Name'
                }
            ),
            'email':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Emeil'
                }
            ),
            'phonenumber':PhoneNumberInternationalFallbackWidget(region='BY',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone'
                }
            ),
            'message':forms.Textarea(
                attrs={
                      #< textarea name = ""id = "message"cols = "30"rows = "7"class ="form-control" placeholder="Message" > < / textarea >
                    'id':'message',
                    'cols':'30',
                    'rows':'7',
                    'class':'form-control',
                    'placeholder': 'Message'
                }
            )
        }