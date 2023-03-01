from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver


gender_choices= (
    ("MALE", "Male"),
    ("FEMALE", "Female"),
)


class IT(models.Model):
    staff = models.OneToOneField('Staff', on_delete=models.CASCADE, primary_key= True, related_name='it_member' )
    specialization = models.CharField(max_length=100, default='unassigned')

    class Meta:
        verbose_name_plural= "IT"


    def __str__(self):
        return f"{self.staff.firstname} {self.staff.lastname} - {self.specialization}"

class Media(models.Model):
    staff = models.OneToOneField('Staff', on_delete=models.CASCADE, primary_key=True, related_name='media_member')
    specialization = models.CharField(max_length=100, default='unassigned')
    class Meta:
        verbose_name_plural = "Media"

    def __str__(self):
        return f"{self.staff.firstname} {self.staff.lastname} - {self.specialization}"

class Admin(models.Model):
    staff = models.OneToOneField('Staff', on_delete=models.CASCADE, primary_key= True, related_name= 'admin_member')
    specialization = models.CharField(max_length=100, default= 'unassigned')
    is_admin= models.BooleanField(default= True)
    class Meta:
        verbose_name_plural = "Admin"

    def __str__(self):
        return f"{self.staff.firstname} {self.staff.lastname} - {self.specialization}"




class Staff(models.Model):
    department_choices=(
    ("ADMIN", "Administration"),
    ("IT", "Information Technology"),
    ("MEDIA", "Media"),
    )

    firstname= models.CharField(max_length= 200, blank= False)
    lastname= models.CharField(max_length= 200, blank= False)
    staff_id= models.CharField(max_length= 100, primary_key= True, unique= True, default= 0)
    phonenumber= PhoneNumberField()
    email_address= models.EmailField()
    department= models.CharField(max_length= 100, choices=department_choices, blank= False)
    gender= models.CharField(max_length=100, choices=gender_choices)
    state_of_origin= models.CharField(max_length= 234, blank= False)
    account_number= models.CharField(max_length= 20, validators=[RegexValidator(r'^\d+$', 'Enter a valid account number')], blank= False)
    bank= models.CharField(max_length= 100, blank= False)
    account_name= models.CharField(max_length= 100, null= False, blank= False)
    
    it = models.OneToOneField(IT, on_delete=models.CASCADE, null=True, blank=True, related_name= 'staff_it')
    media = models.OneToOneField(Media, on_delete=models.CASCADE, null=True, blank=True, related_name= 'staff_media')
    admin = models.OneToOneField(Admin, on_delete=models.CASCADE, null=True, blank=True, related_name='staff_admin')

    def __str__(self):
        return f'{self.staff_id} - {self.department}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.department == 'IT':
            if self.it is None:
                it_obj = IT.objects.create(staff=self)
                self.it = it_obj
                self.save()
        elif self.department == 'Media':
            if self.media is None:
                media_obj = Media.objects.create(staff=self)
                self.media = media_obj
                self.save()
        elif self.department == 'Administration':
            if self.admin is None:
                admin_obj = Admin.objects.create(staff=self)
                self.admin = admin_obj
                self.save()


    










# Create your models here.
