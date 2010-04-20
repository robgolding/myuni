import os
import myuni

FORMAT = u'%(rev)d:%(node)s'
UNKNOWN = u'unknown'

def get_hg_revision(path=None):
	"""
	Returns the Mercurial revision in the form xx:abcd
	where xx is the revision number (e.g. 23) and
	abcd is 1st 4 characters of the revision
	identifier (e.g. fe02).
	
	Returns unknown if anything goes wrong, such as
	not being able to import the mercurial API.
	
	If path is provided, it should be a directory whose
	hg info you want to inspect. If it's not provided,
	this will use the root myuni/ package directory.
	"""
	rev = None
	if path is None:
		path = os.path.abspath(os.path.join(myuni.__path__[0], '..'))
	print path
	try:
		import sys
		import StringIO
		
		# make the mercurial API wsgi compliant by replacing stdin
		save_stdin = sys.stdin
		sys.stdin = StringIO.StringIO('')
		
		from mercurial import ui, hg
		from mercurial.node import hex
	
		repo = hg.repository(ui.ui(), path)
		fctx = repo.filectx(None, 'tip')
	
		rev = FORMAT % {'rev': fctx.rev(), 'node': hex(fctx.node())[:4]}
	
		# put stdin back
		sys.stdin = save_stdin
	except:
		try:
			import re
			branchheads_path = '%s/.hg/branchheads.cache' % path
			try:
				branchheads = open(branchheads_path, 'r').readlines()
			except IOError:
				pass
			else:
				rev_match = re.search('(\w+)\s+(\d+)', branchheads[0].strip())
				if rev_match:
					rev = FORMAT % {'rev': int(rev_match.groups()[1]), 'node': rev_match.groups()[0][:4]}
		except:
			raise
	
	return rev or UNKNOWN
