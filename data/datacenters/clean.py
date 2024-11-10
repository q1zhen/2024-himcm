import csv

with open("data_sorted.csv", "r", newline="", encoding="utf-8") as src:
	reader = csv.reader(src)
	next(reader)
	with open("space_and_power_clean.csv", "w+", newline="", encoding="utf-8") as dst:
		writer = csv.writer(dst)
		writer.writerow(["total_space", "total_power"])
		for line in reader:
			if line[5] != "n/a" and line[7] != "n/a" and float(line[7]) < 100000:
				writer.writerow([line[5], line[7]])