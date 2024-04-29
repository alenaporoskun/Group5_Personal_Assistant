from django import forms
from .models import Contact, Note

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'birthday']
        error_messages = {
            'phone_number': {
                'invalid': "Please enter a valid phone number.",
            },
            'email': {
                'invalid': "Please enter a valid email address.",
            },
        }

class NoteForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите теги через запятую'}), required=False)
    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']
        
