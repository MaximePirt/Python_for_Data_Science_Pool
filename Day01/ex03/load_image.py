import numpy as np
from PIL import Image

def ft_load(path: str) -> np.array:

	im = 0

	if not path.endswith(('.jpg', '.jpeg', '.png')):
		raise ValueError("ValueError: Bad extension")
	try:
		im = Image.open(path)
	except:
		raise ValueError("ValueError: given path doesn't lead to an image, or image cannot be open")
	a = np.array(im)
	print("The shape of image is:", a.shape)


	return a