from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def Home_view(request):
    return render(request,"home.html")

def About_view(request):
    return render(request,"about.html")

def Service_view(request):
    return render(request,"service.html")

def Gallery_view(request):
    return render(request,"gallery.html")

def Contact_view(request):
    return render(request,"contact.html")

def contact(request):
    return render(request,'contact.html')

    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         # Save the form data to database
    #         contact = form.save()
            
    #         # Prepare email content
    #         subject = f'New Contact Form Submission: {contact.get_subject_display()}'
    #         message = f'''
    #         Name: {contact.name}
    #         Email: {contact.email}
    #         Phone: {contact.phone}
    #         Subject: {contact.get_subject_display()}
    #         Message: {contact.message}
            
    #         This message was sent from the contact form on your website.
    #         '''
            
    #         # Send email to school owner
    #         send_mail(
    #             subject,
    #             message,
    #             settings.DEFAULT_FROM_EMAIL,
    #             [settings.CONTACT_EMAIL],  # School owner's email
    #             fail_silently=False,
    #         )
            
    #         messages.success(request, 'Thank you for your message. We will get back to you soon!')
    #         return render(request, 'contact.html', {'form': ContactForm()})
    # else:
    #     form = ContactForm()
    
    # return render(request, 'contact.html', {'form': form})