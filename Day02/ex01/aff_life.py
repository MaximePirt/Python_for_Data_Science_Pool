import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def showing_image(graph, country):
	''' Draw a graph from information, including Country as a name'''
	#Showing Part
	x = graph.index.astype(int)
	y = graph.values
	plt.plot(x, y)
	plt.title(f"{country} Life expectancy Projections")
	plt.xlabel("Year")
	plt.ylabel("Life expectancy")
	plt.show()

def main():
	try:
		country = "France"

		data = load("life_expectancy_years.csv")
		located = data.loc[data["country"] == country, data.columns != "country"]
		graph = located.iloc[0]

		showing_image(graph, country)
	except:
		print("Error")
		return -1
	return 


if __name__ == "__main__":
	main()