import pandas as pd

def load(path: str) -> pd.DataFrame:
	try:
		if not path.endswith("csv"):
			raise TypeError("Error, file isn't in csv format")
		data = pd.read_csv(path)
		print("Loading dataset of dimensions", data.shape)
		return data
	except:
		return None
