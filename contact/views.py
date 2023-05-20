from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contact

"""
class ContactFormView(FormView):

    form_class = ContactForm
    template_name = "contact/contact.html"
    success_url = '/email-sent.html/'

    def form_valid(self, form):
        message = "{message_name} / {message_email} said: ".format(
            message_name=form.cleaned_data.get('name'),
            message_email=form.cleaned_data.get('email'),
            message_mobile=form.cleaned_data.get('phone number'))
        message += "\n\n{0}".format(form.cleaned_data.get('message')),
        send_mail(
            subject=form.cleaned_data.get(
                'Message from Lesjardins.com'
                ).strip(),
            message=message,
            from_email='contact@lesjardins.com',
            recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
        )
        form.save()
        return super(ContactFormView, self).form_valid(form)
"""


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            return HttpResponseRedirect('email-sent')
        else:
            form = ContactForm()
            return HttpResponseRedirect('contact')
        
    return render(request, 'contact/contact.html', {'form': form})


def email_sent(request):
    return render(request, 'contact/email_sent.html')


    """
        send_mail(
            "Message from Lesjardins.com",
            message,
            message_email,
            contact@lesjardins.com
        )

        return render(request, 'contact/contact.html', {
            'message_name',
            'message_email',
            'message_mobile',
            'message'
            })
    else:
        return render(request, 'contact/contact.html', {})
            """
