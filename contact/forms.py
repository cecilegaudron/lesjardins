from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'message_name',
            'message_email',
            'message_mobile',
            'message',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'message_name': 'Enter your name',
            'message_email': 'Add your email address',
            'message_mobile': 'Add your phone number if you want',
            'message': 'Enter your message here',
        }

        self.fields['message_mobile'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
