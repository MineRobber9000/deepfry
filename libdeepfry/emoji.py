import json, os.path

BASEDIR = os.path.dirname(os.path.abspath(__file__))
EMOJIS = os.path.join(BASEDIR,"emojis")

with open(BASEDIR+"/emoji.json") as f: d = json.load(f)

def listEmoji():
	return list(d.keys())

def getImage(name):
	return os.path.join(EMOJIS,d[name])
