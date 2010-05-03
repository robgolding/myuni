import datetime
from django.db import models

class LectureManager(models.Manager):
	def next(self):
		now = datetime.datetime.now()
		qs = self.get_query_set().filter(given_at__gt=now).order_by('given_at')
		return qs[0] if qs else None

class Lecture(models.Model):
	module = models.ForeignKey('course.Module')
	room = models.ForeignKey('campus.Room')
	given_at = models.DateTimeField()
	
	objects = LectureManager()
	
	def __unicode__(self):
		return '%s lecture at %s' % (self.module.code, self.given_at)
