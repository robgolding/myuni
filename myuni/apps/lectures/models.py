import datetime
from django.db import models

class LectureManager(models.Manager):
	def next(self):
		now = datetime.datetime.now()
		qs = self.get_query_set().filter(given_at__gt=now).order_by('given_at')
		return qs[0] if qs else None

class Lecture(models.Model):
	module = models.ForeignKey('course.Module', related_name='lectures')
	room = models.ForeignKey('campus.Room')
	given_at = models.DateTimeField()
	number = models.PositiveIntegerField(editable=False, null=True)
	
	objects = LectureManager()
	
	def _update_numbers_in_series(self):
		lectures = Lecture.objects.filter(module=self.module).order_by('given_at')
		for i, l in enumerate(lectures):
			if i+1 != l.number:
				l.number = i+1
				l.save()
	
	def save(self, *args, **kwargs):
		super(Lecture, self).save(*args, **kwargs)
		self._update_numbers_in_series()
	
	def delete(self, *args, **kwargs):
		super(Lecture, self).delete(*args, **kwargs)
		self._update_numbers_in_series()
	
	def __unicode__(self):
		return '%s Lecture %s' % (self.module.code, self.number or '')
	
	class Meta:
		ordering = ('given_at',)
