import csv
import json

with open("hash-rate.json", "r") as f:
	data = json.load(f)
	with open("cleaned.csv", "w+", encoding="utf-8", newline="") as f:
		writer = csv.writer(f)
		writer.writerow(["days", "unix", "hashrate", "price", "eff"])
		for hashrate, price in zip(data["hash-rate"], data["market-price"]):
			unix = hashrate["x"]
			days = int(unix / (24 * 3600 * 1000) - 14254)
			hr = hashrate["y"]
			p = price["y"]
			eff = p / hr
			writer.writerow([
				days, unix, hr, p, eff
			])
