from libdeepfry.actions import deepfry as deepfryImage
from libdeepfry.actions import splitAndFry
import click
from pymediainfo import MediaInfo

def is_video(filename)
	for track in MediaInfo.parse(filename).tracks:
		if track.track_type == "video":
			return True
	return False

@click.command()
@click.option("--brightness",default=2.0)
@click.option("--saturation",default=3.0)
@click.option("--contrast",default=100)
@click.option("--sharpen",default=3.0)
@click.option("--noise/--no-noise",default=False)
@click.argument("in_image",type=click.Path(exists=True))
@click.argument("out_image",type=click.Path(exists=False))
def deepfry(in_image,out_image):
	if is_video(in_image):
		splitAndFry(in_image,out_image)
	else:
		deepfryImage(in_image,out_image)
