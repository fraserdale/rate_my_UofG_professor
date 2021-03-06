from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# The additional attributes we wish to include.
	picture = models.ImageField(upload_to='media/profile_images', blank=True)

	def __str__(self):
		return self.user.username

class Department(models.Model):
	name = models.CharField(max_length=128, unique=True)

class Subject(models.Model):
	dept = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=128, unique=True)

class Professor(models.Model):
	name = models.CharField(max_length=128, unique=False)
	rating = models.IntegerField(default=1, validators=[ MaxValueValidator(5), MinValueValidator(1)])
	picture = models.ImageField(upload_to='media/profile_images', blank=True)
	subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True)

	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Professor, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'professors'

	def __str__(self):
		return self.name

class Reviews(models.Model):
	date = models.DateTimeField(default=datetime.now)
	createdby = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	prof = models.ForeignKey(Professor, null=True, on_delete=models.CASCADE)
	rating = models.IntegerField(default=1, validators=[ MaxValueValidator(5), MinValueValidator(1)])
	comment = models.CharField(max_length=128, unique=False)
 