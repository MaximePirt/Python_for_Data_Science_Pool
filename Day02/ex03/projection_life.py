import matplotlib.pyplot as plt
from load_csv import load



def showing_image(ytitle):
	''' Draw a graph from previous loaded datas'''
	plt.title(ytitle)
	plt.xlabel("Gross domestic Product")
	plt.ylabel("Life expectancy")
	plt.show()
	return

def main():
	try:
		income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
		life = load("life_expectancy_years.csv")
		years="1900"

		a_graph = income[years]
		b_graph = life[years]

		print((b_graph))
		plt.scatter(a_graph, b_graph)
		plt.xscale('log')
		plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
		showing_image(years)
	except:
		print("Error")
		return -1
	return 


if __name__ == "__main__":
	main()
