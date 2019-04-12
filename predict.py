import cv2
import tensorflow as tf
import numpy as np
import os

CATEGORIES = ["bishopB", "bishopW", "empty", "kingB", "kingW",
			"knightB", "knightW", "pawnB", "pawnW", "queenB",
			"queenW", "rookB", "rookW"]

os.chdir("modelFinal1_img40x40")

def prepare_file(filepath):
	IMG_SIZE = 40
	#img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
	new_array = cv2.resize(filepath, (IMG_SIZE, IMG_SIZE))

	return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def set_piece(nb):
	if nb == 0 :
		return "B"
	elif nb == 1 :
		return "b"
	elif nb == 2 :
		return '.'
	elif nb == 3 :
		return "K"
	elif nb == 4 :
		return "k"
	elif nb == 5 :
		return "C"
	elif nb == 6 :
		return "c"
	elif nb == 7 :
		return "P"
	elif nb == 8 :
		return "p"
	elif nb == 9 :
		return "Q"
	elif nb == 10 :
		return "q"
	elif nb == 11 :
		return "R"
	elif nb == 12 :
		return "r"

model = tf.keras.models.load_model("64x3-CNN.model")

os.chdir("../")

image = cv2.imread('test.jpg', 0)

plateau = [['.']*8 for i in range(8)]

for i in range(8):
	for j in range(8):
		case = image[i*150:(i+1)*150, j*150:(j+1)*150]
		#new_case = case.reshape(-1, 40, 40, 1)
		prediction = model.predict([prepare_file(case)])
		prediction = list(prediction[0])
		print(prediction)
		plateau[i][j] = set_piece(prediction.index(max(prediction)))
		print(prediction.index(max(prediction)))

for i in range(8):
	print(plateau[i])

# cas 1 case
"""

image = "testseen.jpg"
prediction = model.predict([prepare_file(image)])

print(prediction)

#print(CATEGORIES[int(prediction[0][0])])

prediction = list(prediction[0])
print(CATEGORIES[prediction.index(max(prediction))])
"""
