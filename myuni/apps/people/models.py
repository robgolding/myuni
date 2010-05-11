from django.db import models

title_list = ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Prof.']
TITLE_CHOICES = tuple([(c, c) for c in title_list])

class Profile(models.Model):
	user = models.OneToOneField('auth.User')
	
	title = models.CharField(max_length=20, choices=TITLE_CHOICES, null=True, blank=True)
	initial = models.CharField(max_length=10, default='', null=True, blank=True)
	sid = models.CharField(max_length=20, null=True, blank=True)
	
	def get_full_name(self):
		def format(string, format='%s '):
			if string:
				return format % string
			return ''
		
		user = {
			'title': format(self.title),
			'first_name': format(self.user.first_name),
			'last_name': self.user.last_name or '',
			'initial': format(self.initial, '%s. ')
		}
		
		if user['first_name'] and user['last_name']:
			return '%(title)s%(first_name)s%(initial)s%(last_name)s' % user
		return self.user.username
	
	@models.permalink
	def get_absolute_url(self):
		return ('people_user_detail', [self.user.username])
	
	def __unicode__(self):
		return '[Profile] %s' % self.get_full_name()
