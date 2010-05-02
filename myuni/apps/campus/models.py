from django.db import models

class Campus(models.Model):
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name

class Building(models.Model):
	code = models.CharField(max_length=20, unique=True, db_index=True)
	campus = models.ForeignKey(Campus)
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name

class Room(models.Model):
	code = models.CharField(max_length=20, unique=True, db_index=True)
	building = models.ForeignKey(Building)
	name = modle.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name
