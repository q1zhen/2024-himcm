import csv

mix = {}

with open("world-energy-mix-proportion.csv", "r", encoding="utf-8", newline="") as f:
	reader = csv.reader(f)
	next(reader)
	for line in reader:
		if mix.get(line[0]) == None:
			mix[line[0]] = {}
		mix[line[0]][line[1][0]] = [float(i) if i != "n/a" else 0 for i in line[3:]]

result = 0

def code(c):
	if mix.get(c) != None:
		return c
	elif c in ["AM", "AZ", "GE", "KZ", "KG", "RU", "TJ", "TM", "UZ"]:
		return "Non-OECD Europe and Eurasia"
	elif c in ["BH", "IR", "IQ", "JO", "KW", "LB", "OM", "QA", "SA", "SY", "AE", "YE"]:
		return "Middle East"
	elif c in ["MA", "DZ", "NG", "ZA", "MU", "TN", "ET", "MG", "CV", "SD", "KE", "CD", "SC", "TZ", "GH", "LY", "SO", "UG", "NE", "SN", "ML", "GQ", "ZW", "AO", "BF", "CM", "RW", "MZ", "NA", "ER", "BW", "TD", "MR", "GN", "LR", "ZM", "SL", "CI", "BJ", "SZ", "TG", "MW", "GM", "LS", "GA", "DJ", "SS", "BI", "CG", "KM", "EH"]:
		return "Africa"
	else:
		return "World"

def calc(country, power):
	return float(power) * (
		mix[country]["F"][-2] * 768908
		+ mix[country]["N"][-2] * 5068
		+ mix[country]["R"][-2] * 39560
	)

with open("../datacenters/data_sorted_country_codes.csv", "r", encoding="utf-8", newline="") as f:
	reader = csv.reader(f)
	next(reader)
	print("MW * t/TWh")
	for dc in reader:
		country = code(dc[0])
		power = dc[-1]
		if power != "n/a": result += calc(country, power)
	print(result)
