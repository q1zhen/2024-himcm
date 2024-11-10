import csv

with open("data_sorted.csv", "r", newline="", encoding="utf-8") as f:
	reader = csv.reader(f)
	header = next(reader)
	rows = [line for line in reader]

while 1:
	ranges = [*[int(i) for i in input("Enter ranges: ").split()], 1e16]
	counts = {
		k: 0 for k in ranges
	}
	occs = counts.copy()
	# 5 7
	for row in rows:
		if row[5] == "n/a": continue
		for u in ranges:
			if float(row[5]) < u:
				counts[u] += 1
				if row[7] != "n/a":
					occs[u] += 1
				else:
					occs[u] -= 1
				break
	for i in ranges:
		print("<", i, "\t", occs[i], "\t", counts[i], "\t", int(occs[i] / counts[i] * 100), "%")



