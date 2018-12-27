import magick, tempfile, subprocess, tempdir, os

def listdir(dir):
	for file in os.listdir(dir):
		yield os.path.join(dir,file)

def getImageSize(filename):
	return subprocess.check_output("identify {} | cut -d' ' -f3".format(filename),shell=True).decode("ascii").strip()

def deepfry(input,output,brightness=1,saturation=1,contrast=None,sharpen=None,noise=False,emojilocation=[]):
	tf = tempfile.NamedTemporaryFile(suffix="jpg")
	magick.convert(input,tf.name,format="jpg")
	for emoji in emojilocation:
		magick.composite("emojis/"+emoji[0],tf.name,tf.name,format="jpg",geometry="{:+02}{:+02}".format(*emoji[1:]))
	if noise:
		magick.composite("noise.jpg",tf.name,tf.name,blend=20)
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
	for image in listdir(tf.name):
		deepfry(image,image,**kwargs)
	magick.convert(tf.name+"/*.jpg",output)
	os.chmod(output,0o644)
