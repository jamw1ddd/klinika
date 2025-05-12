from django import forms
from .models import Appointment, ContactMessage, Doctor


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'doctor', 'date', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ismingizni kiriting...', 'class': 'appointment-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email manzilingizni kiriting...', 'class': 'appointment-input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon raqamingizni kiriting...', 'class': 'appointment-input'}),
            'doctor': forms.Select(attrs={'class': 'appointment-input'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'appointment-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Xabaringizni bu yerga yozing...', 'class': 'appointment-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a default "Doctorni tanlang..." option
        self.fields['doctor'].empty_label = 'Doktorni tanlang...'


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'subject', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ismingiz', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Mavzu', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email manzilingiz', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon raqamingiz', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Xabaringizni bu yerga yozing...', 'class': 'form-control', 'rows': 5}),
        }
