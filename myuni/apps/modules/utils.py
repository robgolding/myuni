import datetime

FIRST_YEAR = 2005
FUTURE_YEARS = 2

def generate_year_choices(first_year=FIRST_YEAR, current_year=datetime.datetime.today().year, future=FUTURE_YEARS):
	"""Generate model choices for the `year' field. Starts with first_year
	and continues until (current_year + future).
	
	>>> generate_year_choices(first_year=2008, current_year=2010, future=2)
	(('2008-2009', '08/09'), ('2009-2010', '09/10'), ('2010-2011', '10/11'), ('2011-2012', '11/12'), ('2012-2013', '12/13'))
	>>> generate_year_choices(first_year=2010, current_year=2020, future=1)
	(('2010-2011', '10/11'), ('2011-2012', '11/12'))
	"""
	years = []
	for y in range(first_year, current_year + future + 1):
		s = '%s-%s' % (y, y+1)
		t = '%s/%s' % (str(y)[2:], str(y+1)[2:])
		years.append((s,t))
	return tuple(years)
