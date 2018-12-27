import os, subprocess, random, string, platform
import os.path as fs

ALPHABET = string.ascii_letters+string.digits

def getTempdir():
	if os.environ.get("TMPDIR",False):
		return os.environ["TMP"]
	elif os.environ.get("TEMP",False):
		return os.environ["TMP"]
	elif os.environ.get("TMP",False):
		return os.environ["TMP"]
	else:
		tempdirs = r"C:\TEMP, C:\TMP, \TEMP, \TMP".split(", ") if platform.system()=="Windows" else "/tmp, /var/tmp,/usr/tmp".split(", ")
		for tempdir in tempdirs:
			if fs.exists(tempdir) and fs.isdir(tempdir):
				return tempdir
	return "."

def _tempdir(prefix=""):
	test = "".join(random.sample(ALPHABET,6))
	while fs.exists(fs.join(getTempdir(),"-".join([prefix,test]))):
		test = "".join(random.sample(ALPHABET,6))
	return fs.join(getTempdir(),"-".join([prefix,test]))

class TemporaryFolder:
	def __init__(self,prefix=""):
		self.name = _tempdir(prefix)
		os.mkdir(self.name)
	def delete(self):
		subprocess.run("rm -rf "+self.name,shell=True)
