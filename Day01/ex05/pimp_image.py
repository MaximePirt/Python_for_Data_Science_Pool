import matplotlib.pyplot as plt
import numpy as np



def showing_image(img):
	#Showing Part
	plt.imshow(img)
	plt.axis('on')
	plt.show()


def ft_invert(array):
	''' Inverts the color of the image received. '''
	img = array.copy()
	invert = 255 - img
	return showing_image(img)

def ft_red(array):
	''' Change image color to red. '''
	img = array.copy()
	img[:,:,1] = 0
	img[:,:,2] = 0
	return showing_image(img)

def ft_green(array):
	''' Change image color to green. '''
	img = array.copy()
	img[:,:,0] = 0
	img[:,:,2] = 0
	return showing_image(img)

def ft_blue(array):
	''' Change image color to blue. '''
	img = array.copy()
	img[:,:,0] = 0
	img[:,:,1] = 0
	return showing_image(img)

def ft_grey(array):
	'''Change image color to grey. '''
	img = array.copy()
	grey = (img[:,:,0] / 3 + img[:,:,1] / 3 + img[:,:,2] / 3)
	img[:,:,0] = grey
	img[:,:,1] = grey
	img[:,:,2] = grey
	return showing_image(img)
