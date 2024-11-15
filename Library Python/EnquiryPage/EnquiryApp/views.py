from django.shortcuts import render
from .models import EnquiryData

# Create your views here.

def home(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        course = request.POST.get('course')

        # Create and save the EnquiryData object
        enquiry_obj = EnquiryData(name=name, contact=contact, email=email, course=course)
        enquiry_obj.save()  # Save to the database

        # Optionally, pass a success message to the template
        return render(request, 'index.html', {'success': True})

    return render(request, 'index.html')
