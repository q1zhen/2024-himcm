import csv
from math import log, exp

temperature = lambda x: 3.42 * log((422 + 1.279e-4 * (4.7531e-164 * exp(0.1887 * x) + 7.7387e281 * exp(-0.3268 * x) * (x - 2010.6384) ** 6.561)) / 422)

with open("temperature.csv", "w+", newline="", encoding="utf-8") as f:
	writer = csv.writer(f)
	writer.writerow(["year", "temperature"])
	writer.writerow([2010, 0])
	for t in range(2011, 2031):
		writer.writerow([t, temperature(t)])
