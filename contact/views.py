from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Contact


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            return HttpResponseRedirect('email-sent.html')
        else:
            form = ContactForm()
            return HttpResponseRedirect('contact')

    return render(request, 'contact/contact.html', {'form': form})


def email_sent(request):
    return render(request, 'contact/email-sent.html')
