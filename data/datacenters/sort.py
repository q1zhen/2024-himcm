import csv

with open("data.csv", "r", newline="", encoding="utf-8") as f:
	reader = csv.reader(f)
	header = next(reader)
	sorted_rows = sorted(reader, key=lambda row: int(row[0]))

def get_number(s: str):
	if s == "n/a": return s
	r = ""
	for i in s:
		if i not in "1234567890.": break
		r += i
	return r

with open("data_sorted.csv", "w+", newline="", encoding="utf-8") as f:
	writer = csv.writer(f)
	writer.writerow(header)
	for row in sorted_rows:
		for i in [5, 6, 7, 8]:
			row[i] = get_number(row[i])
		writer.writerow(row)
