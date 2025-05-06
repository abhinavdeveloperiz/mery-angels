# from django import forms
# from .models import Contact

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'email', 'phone', 'subject', 'message']
#         widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
#             'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
#             'message': forms.Textarea(attrs={'placeholder': 'Type your message here...', 'rows': 3}),
#         } 