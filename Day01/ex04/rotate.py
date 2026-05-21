from load_image import ft_load, zoom, grayscale
import matplotlib.pyplot as plt
import numpy as np



def rotation(img):
	rows, cols, _ = img.shape
	new_img = np.empty((cols, rows), dtype=img.dtype)

	for i in range(rows):
		for j in range(cols):
			new_img[j, i] = img[i, j, 0]
	return new_img


def showing_image(img):
	#Showing Part
	plt.imshow(img, cmap='grey')
	plt.axis('on')
	plt.show()

def main():
	""" Main function, call loading function then zoom function"""
	a = 0
	try:
		a = ft_load("animal.jpeg")
		a = zoom(a, 100, 500, 450, 850)
		a = grayscale(a)[..., np.newaxis]
		print("The Shape of image is:", a.shape)
		print(a)
		a = rotation(a)
		print("New shape after Transpose:", a.shape)


		print(a)

		showing_image(a)
	except Exception as e:
		print(e)
		return 1


if __name__ == "__main__":
	main()