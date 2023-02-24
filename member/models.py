from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

department_choices=(
    ("ADMIN", "Administration"),
    ("IT", "Information Technology"),
    ("MEDIA", "Media")
)

gender_choices= (
    ("MALE", "Male"),
    ("FEMALE", "Female"),
)

class Staff(models.Model):
    firstname= models.CharField(max_length= 234)
    lastname= models.CharField(max_length= 234)
    phonenumber= PhoneNumberField()
    email_address= models.EmailField( max_length=254)
    department= models.CharField(max_length= 100, choices=department_choices)
    gender= models.CharField(max_length=100, choices=gender_choices)
    state_of_origin= models.CharField(max_length= 234)
    account_number= models.CharField(max_length= 20, validators=[RegexValidator(r'^\d+$', 'Enter a valid account number')])
    bank= models.CharField(max_length= 100)
    account_name= models.CharField(max_length= 234)

class Admin(models.Model):
    pass

class IT(models.Model):
    pass

class Media(models.Model):
    pass
# Create your models here.
