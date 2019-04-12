import numpy as np
import cv2
import os

image = cv2.imread("testout.jpg")
os.chdir("cases")
c = 0

for i in range(8):
	for j in range(8):
		cropped = image[i*150:(i+1)*150, j*150:(j+1)*150]
		os.chdir("/home/arthur/Desktop/get_cam/cases")
		c +=1

		if c==1 or c==8:
			os.chdir("rookB")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)

		elif c==2 or c==7:
			os.chdir("knightB")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)

		elif c==3 or c==6:
			os.chdir("bishopB")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)

		elif c==4:
			os.chdir("queenB")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)

		elif c==5:
			os.chdir("kingB")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)

		elif c in [9, 10, 11, 12, 13, 14, 15, 16]:
			os.chdir("pawnB")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)




		elif c in [49, 50, 51, 52, 53, 54, 55, 56]:
			os.chdir("pawnW")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)

		elif c==58 or c==63:	
			os.chdir("knightW")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)

		elif c==59 or c==62:
			os.chdir("bishopW")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)

		elif c==60:
			os.chdir("queenW")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)

		elif c==61:
			os.chdir("kingW")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)

		elif c==57 or c==64:
			os.chdir("rookW")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)

		else :
			os.chdir("empty")
			nb = len([name for name in os.listdir('.') if os.path.isfile(name)])
			cv2.imwrite("Z"+str(nb)+".jpg", cropped)
