from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_creation(models.Model):
	first_name = models.CharField('First Name',max_length=50)
	last_name = models.CharField('Last Name',max_length=50)
	email = models.EmailField('Email Id')
	password = models.CharField('Password',max_length=50)
	username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

	class Meta:
		verbose_name = "User_create"

	def __str__(self):
		return str(self.username)

class Post(models.Model):
	user = models.ForeignKey(User_creation,on_delete=models.CASCADE)
	text = models.TextField(default="Null")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Post"

	def __str__(self):
		return str(self.user)