from django.shortcuts import render, redirect
from.forms import StaffForm

def home(request):
    return render(request, 'base.html' )

def signup(request):
    staff_form= StaffForm()
    if request.method== "POST":
        staff_form= StaffForm(request.POST)
        if staff_form.is_valid:
            staff=staff_form.save(commit= False)
            staff.save()
            return redirect('home')
    else:
        staff_form= StaffForm()
        
    context={
            'staff_form':staff_form
        }
    return render(request, 'base/registration.html', context)

# Create your views here.
