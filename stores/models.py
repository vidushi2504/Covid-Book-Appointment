from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Store(models.Model):

	user=models.OneToOneField(User, on_delete=models.CASCADE)
	userImage=models.ImageField(upload_to="Store", default="default/default.png", blank=True)
	store_name=models.CharField(max_length=300)
	address1=models.TextField()
	locality = models.TextField()
	city = models.CharField(max_length=300)
	pincode = models.CharField(max_length=300)
	description=models.TextField(blank=True)
	category=models.CharField(max_length=300)
	contact=models.CharField(max_length=300, blank=True)
	openingtime=models.TimeField(blank=True)
	closingtime=models.TimeField(blank=True)
	limit=models.IntegerField()
	date=models.DateField(auto_now_add=True, blank=True)
	store_email=models.TextField()

	def __str__(self):
		return self.store_name

class Time(models.Model):

	store=models.ForeignKey(Store, on_delete=models.CASCADE)
	starttime=models.TimeField()
	endtime=models.TimeField()
	limit=models.IntegerField()

	def __str__(self):
		return self.store.store_name+str(self.id)