import csv

with open("data.csv", "r", newline="", encoding="utf-8") as f:
	reader = csv.reader(f)
	header = next(reader)
	sorted_rows = sorted(reader, key=lambda row: int(row[0]))

with open("data_sorted.csv", "w+", newline="", encoding="utf-8") as f:
	writer = csv.writer(f)
	writer.writerow(header)
	writer.writerows(sorted_rows)
