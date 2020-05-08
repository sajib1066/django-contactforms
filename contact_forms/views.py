from django.http import HttpResponse
from django.contrib import messages

from .models import Contact

def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        try:
            contacts = Contact.objects.create(name=name, email=email, subject=subject, message=message)
            contacts.save()
        except Exception as e:
            return HttpResponse(e)
        success_message = ('Successfully Send Feedback!')
        return HttpResponse(success_message)
    else:
        return HttpResponse('Something Wrong')