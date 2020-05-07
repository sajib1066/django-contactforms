from django.shortcuts import render
from contact_forms.forms import ContactForm

def home(request):
    forms = ContactForm()
    context = {
        'forms': forms
    }
    return render(request, 'home.html', context)
