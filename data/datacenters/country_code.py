import csv
import pycountry

def clean(line):
	return [line[i] for i in [3, 5, 6, 7]]

with open("data_sorted.csv", "r", encoding="utf-8", newline="") as f:
	reader = csv.reader(f)
	header = clean(next(reader))
	lines = [clean(line) for line in reader]

def code(name):
	try:
		country = pycountry.countries.lookup(name)
		return country.alpha_2
	except LookupError:
		print(name)
		return name

with open("data_sorted_country_codes.csv", "w+", encoding="utf-8", newline="") as f:
	writer = csv.writer(f)
	writer.writerow(header)
	for line in lines:
		line[0] = code(line[0])
		writer.writerow(line)
