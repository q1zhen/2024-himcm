import csv

def read(path):
	with open(path, "r", newline="", encoding="utf-8") as f:
		reader = csv.reader(f)
		next(reader)
		return [line for line in reader]

_powers = read("datacenters/by_country.csv")
_mix_fits = read("emissions/mix_fits.csv")

powers = {
	line[0]: float(line[1]) for line in _powers
}

mix_fits = {line[0]: {} for line in _mix_fits}
for line in _mix_fits:
	mix_fits[line[0]][line[1]] = {
		"k": float(line[2]), "b": float(line[3])
	}

pt = 0
for country, power in powers.items():
	pt += power
print("Total power:", pt)

def code(c):
	if mix_fits.get(c) != None:
		return c
	elif c in ["AM", "AZ", "GE", "KZ", "KG", "RU", "TJ", "TM", "UZ"]:
		return "Non-OECD Europe and Eurasia"
	elif c in ["BH", "IR", "IQ", "JO", "KW", "LB", "OM", "QA", "SA", "SY", "AE", "YE"]:
		return "Middle East"
	elif c in ["MA", "DZ", "NG", "ZA", "MU", "TN", "ET", "MG", "CV", "SD", "KE", "CD", "SC", "TZ", "GH", "LY", "SO", "UG", "NE", "SN", "ML", "GQ", "ZW", "AO", "BF", "CM", "RW", "MZ", "NA", "ER", "BW", "TD", "MR", "GN", "LR", "ZM", "SL", "CI", "BJ", "SZ", "TG", "MW", "GM", "LS", "GA", "DJ", "SS", "BI", "CG", "KM", "EH"]:
		return "Africa"
	else:
		return "World"

def sec(t, s):
	r = 0
	for country, power in powers.items():
		k = mix_fits[code(country)][s]["k"]
		b = mix_fits[code(country)][s]["b"]
		r += power * max(0, min(k * t + b, 1))
	return r

with open("ult.csv", "w+", encoding="utf-8", newline="") as f:
	writer = csv.writer(f)
	writer.writerow(["year", "pf", "pn", "pr"])
	for t in range(2010, 2031):
		writer.writerow([
			t,
			sec(t, "F"),
			sec(t, "N"),
			sec(t, "R"),
		])
