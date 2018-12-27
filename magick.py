# A library to run imagemagick from Python.
# By MineRobber9000
# Licensed under MIT

import subprocess, shutil
def pairs(o):
	for k in o:
		yield k,o[k]

def wrapper(cmd,input,output,**kwargs):
	command = [cmd,input]
	for k,v in pairs(kwargs):
		command.extend(["-{}".format(k),str(v)])
	command.append(output)
	return subprocess.run(command)

def convert(input,output,**kwargs):
	wrapper(shutil.which("convert"),input,output,**kwargs)

def composite(overlay,bg,output,**kwargs):
	command = [shutil.which("composite")]
	for k,v in pairs(kwargs):
		command.extend(["-{}".format(k),str(v)])
	command.extend([overlay,bg,output])
	return subprocess.run(command)
