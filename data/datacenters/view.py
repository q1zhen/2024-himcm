import csv
import os

with open("data.csv", "r", newline="", encoding="utf-8") as f:
	reader = csv.reader(f)
	header = next(reader)
	rows = [line for line in reader]

while 1:
	os.system("cls")
	print("  ".join([f"[{i}] {prop}" for i, prop in enumerate(header)]))
	choice = int(input("> "))
	count = {}
	for row in rows:
		occ = row[choice]
		if occ in count: count[occ] += 1
		else: count[occ] = 1
	sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
	for k, v in sorted_count:
		print(f"{k.ljust(60)}{v}")
	os.system("pause")
