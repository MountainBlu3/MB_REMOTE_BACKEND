from django.db import models
from django.core.validators import RegexValidator, BaseValidator
from phonenumber_field.modelfields import PhoneNumberField



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
    class Meta:
        verbose_name_plural = "Admins"

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
    

    def __str__(self):
        return self.staff_id

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.department == "IT":
            it_member = IT.objects.create(staff=self)
            it_member.save()
        elif self.department == "ADMIN":
            admin_member = Admin.objects.create(staff=self)
            admin_member.save()
        elif self.department == "MEDIA":
            media_member = Media.objects.create(staff=self)
            media_member.save()




    


    




# Create your models here.
