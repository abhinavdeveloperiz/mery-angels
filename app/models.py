# from django.db import models

# # Create your models here.

# class Contact(models.Model):
#     SUBJECT_CHOICES = [
#         ('admission', 'Admission Inquiry'),
#         ('tour', 'School Tour Request'),
#         ('daycare', 'Day Care Inquiry'),
#         ('transport', 'Transportation Inquiry'),
#         ('feedback', 'Feedback'),
#         ('other', 'Other'),
#     ]

#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.name} - {self.subject}"

#     class Meta:
#         ordering = ['-created_at']
