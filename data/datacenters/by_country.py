import csv

with open("data_sorted_country_codes.csv", "r", newline="", encoding="utf-8") as src:
	reader = csv.reader(src)
	next(reader)
	data = {}
	for line in reader:
		country = line[0]
		power = line[3]
		if power == "n/a" or float(power) > 100000: continue
		if data.get(country) == None:
			data[country] = 0
		data[country] += float(power)

with open("by_country.csv", "w+", newline="", encoding="utf-8") as dst:
	writer = csv.writer(dst)
	writer.writerow(["country", "total_power"])
	for c, p in data.items():
		writer.writerow([c, p])