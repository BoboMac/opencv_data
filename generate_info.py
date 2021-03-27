from PIL import Image
import os

outf = open("pos.txt", "w")
dir = "pos"
for f in os.scandir(dir):
	line = ""
	filename = f.name
	img = Image.open(dir + "\\" + filename)
	line = ("pos/" + filename + " 0 0 " + str(img.size[0]) + " " + str(img.size[1]) + "\n")
	outf.write(line)
	print(line)

