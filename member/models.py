from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


gender_choices= (
    ("MALE", "Male"),
    ("FEMALE", "Female"),
)


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
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if self.department == 'Administration':
    #         IT.objects.create(staff=self)
    #     elif self.department == 'Media':
    #         Media.objects.create(staff=self)
    #     elif self.department == 'Administration':
    #         Admin.objects.create(staff=self)
    
    # def __init__(self, *args, **kwargs):
    #     super(Staff, self).__init__(*args, **kwargs)
    #     self._meta.get_field('Id').max_length= len(self.firstname)+ len(self.lastname) + len(valid_key)
    

class IT(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE, related_name='it_staff', primary_key= True)
    specialization = models.CharField(max_length=100, default='unassigned', null= True)

class Media(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE, related_name='media_staff' , primary_key= True)
    specialization = models.CharField(max_length=100, default='unassigned', null= True)



class Admin(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE, related_name='admin_staff' , primary_key= True)
    specialization = models.CharField(max_length=100, default= 'unassigned', null= True)




@receiver(post_save, sender=Staff)
def create_subclass(sender, instance, created, **kwargs):
    if created:
        if instance.department == 'IT':
            IT.objects.create(staff=instance)
        elif instance.department == 'Media':
            Media.objects.create(staff=instance)
        elif instance.department == 'Admin':
            Admin.objects.create(staff=instance)

def update_subclass(sender, instance, **kwargs):
    try:
        it = instance.it_staff
        it.speciality = instance.speciality
        it.save()
    except IT.DoesNotExist:
        pass

    try:
        media = instance.media_staff
        media.media_type = instance.media_type
        media.save()
    except Media.DoesNotExist:
        pass

    try:
        admin = instance.admin_staff
        admin.admin_role = instance.admin_role
        admin.save()
    except Admin.DoesNotExist:
        pass

@receiver(post_delete, sender=Staff)
def delete_subclass(sender, instance, **kwargs):
    try:
        instance.it_staff.delete()
    except IT.DoesNotExist:
        pass

    try:
        instance.media_staff.delete()
    except Media.DoesNotExist:
        pass

    try:
        instance.admin_staff.delete()
    except Admin.DoesNotExist:
        pass
# class Admin(Staff):
#     admin_role= models.CharField(max_length=100, blank= False, null= True)

#     def role(self):
#         admin_staff= Admin(firstname= self.firstname, lastname= self.lastname, ID= self.Id, phonenumber= self.phonenumber, 
#                         email_address= self.email_address, department= self.department, gender= self.gender, state= self.state_of_origin,
#                         account_number= self.account_number, bank= self.bank, account_name= self.account_name, admin_role= self.admin_role)
#         if self.department == 'Adminitstration':
#             admin_staff.save()
#         else:
#             pass
    
#     def __str__(self):
#         return self.ID
# class IT(Staff):
#     It_role= models.CharField(max_length= 100, blank= False, null= True)

#     def role(self):
#         it_staff= IT(firstname= self.firstname, lastname= self.lastname, ID= self.Id, phonenumber= self.phonenumber, 
#                         email_address= self.email_address, department= self.department, gender= self.gender, state= self.state_of_origin,
#                         account_number= self.account_number, bank= self.bank, account_name= self.account_name, It_role= self.It_role)
#         if self.department == "Information Technology":
#             it_staff.save()
#         else:
#             pass
    
#     def __str__(self):
#         return self.ID
        

# class Media(Staff):
#     media_role= models.CharField(max_length=234, blank= False, null= True)

#     def role(self):
#         media_staff= Media(firstname= self.firstname, lastname= self.lastname, ID= self.Id, phonenumber= self.phonenumber, 
#                         email_address= self.email_address, department= self.department, gender= self.gender, state= self.state_of_origin,
#                         account_number= self.account_number, bank= self.bank, account_name= self.account_name, media_role= self.media_role)
#         if self.department== "Media":
#             media_staff.save()
#         else:
#             pass


# Create your models here.
