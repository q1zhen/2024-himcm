import csv
import os
import random

with open("data_sorted.csv", "r", newline="", encoding="utf-8") as f:
	reader = csv.reader(f)
	header = next(reader)
	rows = [line for line in reader]

while 1:
	os.system("cls")
	print("  ".join([f"[{i}] {prop}" for i, prop in enumerate(header)]))
	choice = int(input("> "))
	os.system("cls")
	print(f"For {header[choice]}, do:", "  ".join([f"[{i}] {prop}" for i, prop in enumerate(["list", "data", "distribution", "latex"])]))
	cmd = int((input("> ")))
	if cmd == 0:
		count = {}
		for row in rows:
			occ = row[choice]
			if occ in count: count[occ] += 1
			else: count[occ] = 1
		sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
		for k, v in sorted_count:
			print(f"{k.ljust(60)}{v}")
	elif cmd == 1:
		limit = float(input("Upper limit: "))
		items = [float(row[choice]) for row in rows if row[choice] != "n/a" and float(row[choice]) <= limit]
		print()
		print("Sum:", sum(items))
		print("Avg:", sum(items) / len(items))
	elif cmd == 2:
		items = list(set([float(row[choice]) for row in rows if row[choice] != "n/a"]))
		items = sorted(items)
		for i in items: print(i)
	elif cmd == 3:
		def str_row(id: int, row: list):
			name = row[1]
			for i in range(len(name)):
				if i >= 8 and name[i] == " ": break
			name = name[:i]
			address = row[4].split(", ")
			address = f"{address[-2]}, {address[-1]}"
			space = row[5]
			power = row[7]
			return f"{id} & {name} ... & ..., {address} & {space} & {power} \\\\"
		for id in range(11):
			r = "n/a"
			while "n/a" in r:
				r = str_row(id, rows[random.randint(0, 4300)])
			print(r)
	os.system("pause")
