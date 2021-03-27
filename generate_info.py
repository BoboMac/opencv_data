from PIL import Image
import os

outf = open("pos.txt", "w")
dir = "pos"
for f in os.scandir(dir):
	line = ""
	filename = f.name
	img = Image.open(dir + "/" + filename)
	line = ("pos/" + filename + " 1 0 0 " + str(img.size[0]) + " " + str(img.size[1]) + "\n")
	outf.write(line)
	print(line)
outf.close()

# negatives
noutf = open("neg.txt", "w")
dir = "neg"
for f in os.scandir(dir):
	line = ""
	filename = f.name
	line = ("neg/" + filename + "\n")
	noutf.write(line)
	print(line)
