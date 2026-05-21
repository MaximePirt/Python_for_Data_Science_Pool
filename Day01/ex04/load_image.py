from PIL import Image
from scipy import ndimage, datasets
import numpy as np



def ft_load(path: str) -> np.array:

	im = 0
	try:
		im = Image.open(path)
	except:
		print("ValueError: given path doesn't lead to an image, or image cannot be open")
		return
	a = np.array(im)

	return a

def grayscale(img):
	grey = img[:, :, 0]
	# [..., np.newaxis]
	return grey



def zoom(img, y_start, y_end, x_start, x_end):
	""" Cut image to center as a "zoom" 
		input : img - image array (using numpy)
		{
			y_start, y_end -
			x_start, x_end -
		} Zooming coordonate, up - down, left-right
	"""

	#"Zooming" part
	crop_img = img[y_start:y_end, x_start:x_end]

	return crop_img



# [400-55] [940-55]
# [400 - 470] [940-470]