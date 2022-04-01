from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

class User(AbstractUser):
    phone=models.CharField(max_length=10,null=True,blank=True)


class userProfile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	bio=models.CharField(max_length=200,null=True,blank=True)
	gender=models.CharField(max_length=7,null=True,blank=True)
	dob=models.DateField(null=True,blank=True)
	address=models.CharField(max_length=100,null=True,blank=True)
	profile_picture=models.ImageField(default='image/profile_picture/default.jpeg',upload_to='image/profile_picture')
	created=models.DateTimeField(default=timezone.now)

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		img=Image.open(self.profile_picture.path)

		if img.height>200 or img.width>200:
			new_image=(200,200)
			img.thumbnail(new_image)
			img.save(self.profile_picture.path)

	def __str__(self):
		return str(self.user)



class OTP(models.Model):
	number = models.CharField(max_length=10,null=True,blank=True)
	otp = models.CharField(max_length=6,null=True,blank=True)
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.number)



