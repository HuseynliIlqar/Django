from django import forms
from .models import (Contact, EmailSubscription,
                     CourseRegistration,Comment)

class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = CourseRegistration
        fields = ['phone', 'experience', 'bio']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Your Message', 'rows': 4}),
        }

class EmailSubscriptionForm(forms.ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Your Email'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control border-0 p-4',
                    'placeholder': 'Rəyinizi buraya yazın...'
                }
            ),
        }