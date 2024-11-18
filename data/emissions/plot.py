import csv

with open("world-energy-mix-proportion.csv", "r", encoding="utf-8", newline="") as f:
	reader = csv.reader(f)
	header = next(reader)
	lines = [line for line in reader]

result = [[i] for i in header]
for line in lines:
	for i in range(len(line)):
		result[i].append(line[i])
	result[0][-1] = f"{line[0]}_{line[1][0]}"

with open("world_mix_plot.csv", "w+", encoding="utf-8", newline="") as f:
	writer = csv.writer(f)
	writer.writerows(result)