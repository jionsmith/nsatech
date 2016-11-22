from django.db import models
from django.conf import settings
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

class Venu(models.Model):
	google_place_id = models.CharField(max_length=200)
	venu_name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=50)
	trading_hours = models.TextField()
	desc = models.TextField()
	
	def __str__(self):
		return self.venu_name    		

	def get_absolute_url(self):
		return u'/dashboard/'

class Occupation(models.Model):
	venu = models.ForeignKey(Venu, on_delete=models.CASCADE)
	day_num = models.CharField(max_length=20)
	time = models.IntegerField()
	value = models.IntegerField()
	create_date = models.DateField(default=date.today)

class Event(models.Model):
	venu = models.ForeignKey(Venu, on_delete=models.CASCADE)
	event_name = models.CharField(max_length=200)
	event_description = models.TextField()
	event_date = models.DateField(default=timezone.now)
	event_time = models.TimeField(default=timezone.now)

	def __str__(self):
		return self.event_name    	

	def get_absolute_url(self):
		return u'/dashboard/'