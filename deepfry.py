import libdeepfry as df
import argparse

parser = argparse.ArgumentParser(prog="deepfry.py",description="Deepfries an image.")
parser.add_argument("-b","--brightness",nargs="?",default=1,type=int,help="Brightness multiplier of image.")
parser.add_argument("-s","--saturation",nargs="?",default=1,type=int,help="Saturation multiplier of image.")
parser.add_argument("-c","--contrast",nargs="?",type=int,help="Contrast percentage")
parser.add_argument("-n","--noise",action="store_true",help="Whether or not to add noise to the image")
parser.add_argument("-x","--sharpen",nargs="?",type=int,help="The gamma of sharpen.")
parser.add_argument("-e","--emoji",nargs="?",default=0,type=int,help="How many random emoji to add to the image in random places.")
parser.add_argument("input",help="The image to deepfry.")
parser.add_argument("output",help="The output.")
args = parser.parse_args()
df.deepfry(args.input,args.output,brightness=args.brightness,saturation=args.brightness,contrast=args.contrast,sharpen=args.sharpen,noise=args.noise,emojicount=args.emoji)
