from django.db import models

import utils

# models not finalised yet, just a possible way to do things

MODULE_TYPE_CHOICES = (
	('single-semester', 'Single semester'),
	('full-year', 'Full-year'),
)

YEAR_CHOICES = utils.generate_year_choices()

SEMESTER_CHOICES = (
	('autumn', 'Autumn Semester'),
	('spring', 'Spring Semester'),
    ('summer', 'Summer Semester'),
    ('full-year', 'Full-year'),
)

class ModuleDefinition(models.Model):
	code = models.CharField(max_length=6, unique=True)
	name = models.CharField(max_length=200)
	credits = models.IntegerField(max_length=4)
	level = models.IntegerField(max_length=2)
	type = models.CharField(max_length=30, choices=MODULE_TYPE_CHOICES)
	
	def __unicode__(self):
		return '%s: %s' % (self.code, self.name)
	
	class Meta:
		ordering = ['code', 'name']

class Module(models.Model):
	code    =	property(lambda s: s._get_definition_property('code'))
	name    =	property(lambda s: s._get_definition_property('name'))
	credits =	property(lambda s: s._get_definition_property('credits'))
	level   =	property(lambda s: s._get_definition_property('level'))
	
	definition = models.ForeignKey('ModuleDefinition')
	semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)
	year = models.CharField(max_length=20, choices=YEAR_CHOICES)
	
	convener = models.ForeignKey('auth.User', related_name='modules_convened')
	students = models.ManyToManyField('auth.User', blank=True, related_name='modules_taken')
	
	date_added = models.DateTimeField(auto_now_add=True)
	
	def _get_definition_property(self, property):
		return self.definition.__getattribute__(property)
	
	@models.permalink
	def get_absolute_url(self):
		return ('modules_module_detail', [self.year, self.semester, self.definition.code])
	
	def __unicode__(self):
		return '%s (%s %s)' % (self.definition.code, self.get_semester_display(), self.get_year_display())
	
	class Meta:
		unique_together = (('definition', 'year', 'semester'),)
		get_latest_by = 'date_added'
