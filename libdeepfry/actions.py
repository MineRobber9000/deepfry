import tempfile, subprocess, os, random
from libdeepfry import magick, tempdir, emoji

RAW_DIR = os.path.dirname(os.path.abspath(__file__))

def listdir(dir):
	for file in os.listdir(dir):
		yield os.path.join(dir,file)

def getImageSize(filename):
	return subprocess.check_output("identify {} | cut -d' ' -f3".format(filename),shell=True).decode("ascii").strip()

def deepfry(input,output,brightness=1,saturation=1,contrast=None,sharpen=None,noise=False,emojicount=0):
	tf = tempfile.NamedTemporaryFile(suffix="jpg")
	magick.convert(input,tf.name,format="jpg")
	if emojicount>0:
		size = [int(x) for x in getImageSize(tf.name).split("x")]
		for i in range(emojicount):
			em = emoji.getImage(random.choice(emoji.listEmoji()))
			x = random.randint(0,size[0])
			y = random.randint(0,size[1])
			magick.composite(em,tf.name,tf.name,format="jpg",geometry="{:+02}{:+02}".format(x,y))
	if noise:
		magick.composite(os.path.join(RAW_DIR,"noise.jpg"),tf.name,tf.name,blend=20)
	magick.convert(tf.name,tf.name,modulate="{},{},100".format(int(round(brightness*100)),int(round(saturation*100))),quality="1%")
	if contrast is not None:
		magick.convert(tf.name,tf.name,level="{}%".format(contrast))
	if sharpen is not None:
		magick.convert(tf.name,tf.name,sharpen="0x{}".format(sharpen))
	magick.convert(tf.name,output)
	tf.close()

def splitAndFry(video,output,**kwargs):
	tf = tempdir.TemporaryFolder("deepfry")
	magick.convert(video,tf.name+"/deepfry-%05d.jpg")
	total = len(os.listdir(tf.name))
	i = 0
	for image in listdir(tf.name):
		i+=1
		print("\rDeepfrying {!s} of {!s}".format(i,total),end="")
		deepfry(image,image,**kwargs)
	magick.convert(tf.name+"/*.jpg",output)
	os.chmod(output,0o644)
