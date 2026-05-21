import numpy as np
from PIL import Image

def ft_load(path: str) -> np.array:

	im = 0
	try:
		im = Image.open(path)
	except:
		print("ValueError: given path doesn't lead to an image, or image cannot be open")
		return
	a = np.array(im)
	print("The shape of image is:", a.shape)


	return a