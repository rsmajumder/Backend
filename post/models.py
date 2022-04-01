from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
User=settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    followers = models.ManyToManyField(User,related_name="followers",blank=True)
    followings = models.ManyToManyField(User,related_name="followings",blank=True)

class Post(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	caption=models.TextField(max_length=200)
	post_picture=models.FileField(upload_to='image/post_picture',null=True,blank=True)
	likes_user=models.ManyToManyField(User,related_name='likes_user')
	created=models.DateTimeField(default=timezone.now)
	#public,Allfriend,private
	def __str__(self):
		return str(self.user)

class Share(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	caption=models.TextField(max_length=200)
	post=models.ForeignKey(Post,on_delete=models.CASCADE)
	likes_user=models.ManyToManyField(User,related_name='_share_likes_user')
	created=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.user)

class Reels(models.Model):
	owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	content=models.CharField(max_length=4000)
	reels_file=models.FileField(upload_to='image/reels_picture',null=True,blank=True)
	reels_date=models.DateField(auto_now_add=True)
	likes = models.ManyToManyField(User,blank=True)
    
	def __str__(self):
		return str(self.owner)
	

class Story(models.Model):
	
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    story = models.ImageField(upload_to='image/storys_picture',null=True,blank=True)
    story_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.profile)

class Comment(models.Model):
	post=models.ForeignKey(Post,on_delete=models.CASCADE)
	text=models.CharField(max_length=200,null=True,blank=True)
	commenter=models.ForeignKey(User,on_delete=models.CASCADE)
	created=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.text)+""+str(self.post)