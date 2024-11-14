import csv

with open("world-energy-mix.csv", "r", encoding="utf-8") as f:
	reader = csv.reader(f)
	next(reader)
	lines = [line for line in reader]

for i in [0, 1, 2, 3, 4, 5, 6, 7, -1]:
	l = lines[i]
	print(f"{l[0]} & {l[1]} & {l[3]} & {l[4]} & $\\cdots$ & {l[-2]} & {l[-1]} \\\\")
