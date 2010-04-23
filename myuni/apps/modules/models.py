from django.db import models

# models not finalised yet, just a possible way to do things

class Module(models.Model):
	code = models.CharField(max_length=6, unique=True)
	name = models.CharField(max_length=200)
	credits = models.IntegerField(max_length=4)
	level = models.IntegerField(max_length=2)
	
	def get_current_teaching(self):
		return Teaching.objects.get(module=self, semester=Semester.objects.current()) or None
	
	def __unicode__(self):
		return '%s: %s' % (self.code, self.name)
	
	class Meta:
		ordering = ['code', 'name']

class Teaching(models.Model):
	module = models.ForeignKey('Module')
	semester = models.ForeignKey('scheduling.Semester')
	convener = models.ForeignKey('auth.User')
	
	def __unicode__(self):
		return '%s (%s)' % (self.module.code, self.semester)
	
	class Meta:
		unique_together = (('module', 'semester'),)