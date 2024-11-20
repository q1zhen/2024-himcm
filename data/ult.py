import csv
from math import *

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

def clamp(x):
	return max(0, min(x, 1))

def sec(t, s):
	r = 0
	for country, power in powers.items():
		k = mix_fits[code(country)][s]["k"]
		b = mix_fits[code(country)][s]["b"]
		r += power * clamp(k * t + b)
	return r

with open("ult.csv", "w+", encoding="utf-8", newline="") as f:
	writer = csv.writer(f)
	writer.writerow(["year", "pf", "pn", "pr", "mf", "mn", "mr", "t", "half", "all", "expansion"])
	for t in range(2011, 2031):
		data = [
			t,
			sec(t, "F"),
			sec(t, "N"),
			sec(t, "R"),
			clamp(-0.0062 * t + 13.2188),
			clamp(-0.0019 * t + 3.9356),
			clamp(0.0082 * t - 16.3568),
		]
		data.append(3.42 * log((422 + 1.279e-4 * 
			((data[1] * 768908 + data[2] * 5068 + data[3] * 39560) * exp(0.1887 * (t - 2024)) * 8760 * 0.13 * 1e-12 + (data[4] * 768908 + data[5] * 5068 + data[6] * 39560) * 7.7387e281 * exp(-0.3268 * t) * pow(t - 2010.6384, 6.561) * 1.7 * 1e-6)
		) / 422))
		data.append(3.42 * log((422 + 1.279e-4 * 
			(((309160 * 0.5 - data[2]) * 768908 + data[2] * 5068 + 309160 * 0.5 * 39560) * exp(0.1887 * (t - 2024)) * 8760 * 0.13 * 1e-12 + (data[4] * 768908 + data[5] * 5068 + data[6] * 39560) * 7.7387e281 * exp(-0.3268 * t) * pow(t - 2010.6384, 6.561) * 1.7 * 1e-6)
		) / 422))
		data.append(3.42 * log((422 + 1.279e-4 * 
			(309160 * 39560 * exp(0.1887 * (t - 2024)) * 8760 * 0.13 * 1e-12 + (data[4] * 768908 + data[5] * 5068 + data[6] * 39560) * 7.7387e281 * exp(-0.3268 * t) * pow(t - 2010.6384, 6.561) * 1.7 * 1e-6)
		) / 422))
		size = lambda x: 7.7387e281 * exp(-0.3268 * x) * pow(max(0, x - 2010.6384), 6.561) + 4.7531e-164 * exp(0.1887 * x)
		data.append((size(t) / size(2023) - 1) * 0.95 + 1)
		writer.writerow(data)
