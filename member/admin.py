from django.contrib import admin
from .models import Staff, IT, Media, Admin

admin.site.register(Staff)
admin.site.register(IT)
admin.site.register(Media)
admin.site.register(Admin)

# Register your models here.
