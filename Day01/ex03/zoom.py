import numpy as np
from load_image import ft_load
from scipy import ndimage, datasets
import matplotlib.pyplot as plt
from PIL import Image


def zoom(img):
	""" Cut image to center + grayscale it before printing"""
	crop_img = img[100:500, 450:850]

	grey = crop_img[:, :, 0][..., np.newaxis]
	print("New shape after slicing:", grey.shape)
	print(grey)

	plt.imshow(grey, cmap='grey')
	plt.axis('on')
	plt.show()


def main():
	""" Main function, call loading function then zoom function"""
	a = 0
	try:
		a = ft_load("animal.jpeg")
		print(a)
		zoom(a)
	except Exception as e:
		print(e)
		return 1


if __name__ == "__main__":
	main()

# [400-55] [940-55]
# [400 - 470] [940-470]