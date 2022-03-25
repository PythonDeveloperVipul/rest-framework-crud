from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail 
from django.conf import settings 

gender=(('male','male'),('female','female'))
# Create your models here.
class ClassRoom(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Student(models.Model):
    classroom=models.ForeignKey(ClassRoom,on_delete=models.CASCADE,related_name="classroom")
    student_name=models.CharField(max_length=125,verbose_name='student name')
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    gender=models.CharField(max_length=6,choices=gender)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)
    address=models.TextField()
    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(c.name for c in self.classroom.all()),
        )


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="http://127.0.0.1:8001/"),
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email],

        fail_silently=False
    )

    