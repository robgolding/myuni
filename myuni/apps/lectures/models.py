from django.db import models

from myuni.apps.course.models import Module

class Lecture(models.Model):
	module = models.ForeignKey('course.Module')
	room = models.ForeignKey('campus.Room')
	given_at = models.DateTimeField()
	
	def __unicode__(self):
		return '%s lecture at %s' % (self.module.code, self.given_at)
