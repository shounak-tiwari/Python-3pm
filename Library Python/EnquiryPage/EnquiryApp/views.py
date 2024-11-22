from django.shortcuts import render,get_object_or_404
from .models import EnquiryData
from django.http import HttpResponse
# Create your views here.

def main(request):
    return render(request,'main.html')



def login(request):
    return render(request,'login.html')


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact_inp = request.POST.get('contact')
        email = request.POST.get('email')
        course = request.POST.get('course')
        # Create and save the EnquiryData object
        filterdata = EnquiryData.objects.filter(contact= contact_inp,email = email)        
        
        if filterdata:

            return render(request, 'index.html',{'success':"number is already registered "})


        enquiry_obj = EnquiryData(name=name, contact=contact_inp, email=email, course=course)
        enquiry_obj.save()  # Save to the database

        # Optionally, pass a success message to the template
        return render(request, 'index.html', {'success': "We will call back your shortly"})

    return render(request, 'index.html')


def Student_record(request):

    if request.method =="POST":
        filterobj = request.POST.get('contact')

        filterdata = EnquiryData.objects.filter(contact= filterobj)        
        
        return render(request,'Record.html',{'filterdata':filterdata})
    else:
        return render(request,'Record.html')

    

