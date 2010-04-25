import datetime

STARTING_YEAR = 2005
FUTURE_YEARS = 2

def generate_year_choices():
    this_year = datetime.datetime.today().year
    years = []
    for y in range(STARTING_YEAR, this_year + FUTURE_YEARS + 1):
        s = '%s-%s' % (y, y+1)
        t = '%s/%s' % (str(y)[2:], str(y+1)[2:])
        years.append((s,t))
    return tuple(years)