#rotates and flips a picture for more test data

import cv2
import sys
import random
import glob

count = 0
FILENAME = 'pos'

def process(pic,output):
	global count

	img = cv2.imread(pic)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	for i in range(30):
		count+=1
		cv2.imwrite(output + '/' + FILENAME + str(count) + '.png',img)

		count+=1
		flip0 = cv2.flip(img,0)
		cv2.imwrite(output + '/' + FILENAME + str(count) + '.png',flip0)

		count+=1
		flip1 = cv2.flip(img,1)
		cv2.imwrite(output + '/' + FILENAME + str(count) + '.png',flip1)

		(rows,cols) = img.shape[:2]

		M = cv2.getRotationMatrix2D(	(cols/2,rows/2),random.randint(8,15),1)
		img = cv2.warpAffine(img,M,(cols,rows))

	print(count)


if __name__ == "__main__":
	inputfolder = sys.argv[1]
	outputfolder = sys.argv[2]

	inp = glob.glob('%s/*.png' % inputfolder)

	for innie in inp:
		process(innie,outputfolder)
