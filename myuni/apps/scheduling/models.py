from django.db import models

SEMESTER_TYPES = (
	('autumn', 'Autumn'),
	('spring', 'Spring'),
)

# these models (and even this app) might not actually be required at all

class Year(models.Model):
    year = models.CharField(max_length=9, unique=True)

    def __unicode__(self):
        return self.year

class Semester(models.Model):
    year = models.ForeignKey(Year)
    type = models.CharField(max_length=20, choices=SEMESTER_TYPES)

    def __unicode__(self):
     return '%s %s' % (self.get_type_display(), self.year)

    class Meta:
        unique_together = (('year', 'type'),)