import matplotlib.pyplot as plt
from load_csv import load

def convert_population(value):
	''' Convert data from csv into real millions or thousands'''
	if value.endswith("M"):
		number = float(value[:-1]) * 1_000_000
	elif value.endswith("k"):
		number = float(value[:-1]) * 1_000
	else:
		number = float(value)
	return number


def loading_graph(graph, country):
	''' Load datas into graph '''
	y = [convert_population(value) for value in graph.values]
	x = [int(year) for year in graph.index]
	plt.plot(x, y, label=country)


def showing_image():
	''' Draw a graph from previous loaded datas'''
	plt.title("Population Projections")
	plt.xlabel("Year")
	plt.ylabel("Population (in Scientific Notation)")
	plt.legend()
	plt.show()
	return

def main():
	try:
		a_country = "France"
		b_country = "Belgium"

		data = load("population_total.csv")

		years = [col for col in data.columns if col != "country" and col.isdigit() and 1800 <= int(col) <= 2050]
		a_graph = data.loc[data["country"] == a_country, years].iloc[0]
		b_graph = data.loc[data["country"] == b_country, years].iloc[0]

		print((a_graph.values))
		loading_graph(a_graph, a_country)
		loading_graph(b_graph, b_country)
		showing_image()
	except:
		print("Error")
		return -1
	return 


if __name__ == "__main__":
	main()