import csv
import pycountry

with open("world-energy-mix.csv", "r", encoding="utf-8", newline="") as f:
	reader = csv.reader(f)
	header = next(reader)
	lines = [line for line in reader]

def code(name):
	try:
		country = pycountry.countries.lookup(name)
		return country.alpha_2
	except LookupError:
		print(name)
		return name

def calc(s, t):
	if s == ".." or t == "..":
		return -1
	sect = int(s)
	total = int(t)
	return sect / total

with open("world-energy-mix-proportion.csv", "w+", encoding="utf-8", newline="") as f:
	writer = csv.writer(f)
	writer.writerow(header)
	for i in range(0, len(lines), 4):
		for j in range(i, i + 3):
			data = lines[j]
			data[0] = code(data[0])
			for col in range(3, len(data)):
				r = calc(data[col], lines[i + 3][col])
				data[col] = r if r != -1 else "n/a"
			writer.writerow(data)
