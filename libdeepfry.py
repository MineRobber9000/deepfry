import magick, tempfile, subprocess

def getImageSize(filename):
	return subprocess.check_output("identify {} | cut -d' ' -f3".format(filename),shell=True).decode("ascii").strip()

def deepfry(input,output,brightness=1,saturation=1,contrast=None,sharpen=None,noise=False,emojilocation=[]):
	tf = tempfile.NamedTemporaryFile(suffix="jpg")
	magick.convert(input,tf.name,format="jpg")
	for emoji in emojilocation:
		magick.composite("emojis/"+emoji[0],tf.name,tf.name,format="jpg",geometry="{:+02}{:+02}".format(*emoji[1:]))
	if noise:
		magick.composite("noise.jpg",tf.name,tf.name,blend=20)
	magick.convert(tf.name,tf.name,modulate="{}00,{}00,100".format(brightness,saturation),quality="1%")
	if contrast is not None:
		magick.convert(tf.name,tf.name,level="{}%".format(contrast))
	if sharpen is not None:
		magick.convert(tf.name,tf.name,sharpen="0x{}".format(sharpen))
	magick.convert(tf.name,output)
	tf.close()
