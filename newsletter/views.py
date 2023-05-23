from django.shortcuts import render
from django.contrib import messages
from .forms import NewsletterForm
from .models import Newsletter


def subscription(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        print(email)
        messages.success(request, "Thank you for your subscription!")

    return render(request, 'home')
