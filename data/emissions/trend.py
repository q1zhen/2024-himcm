import csv

def linear_regression(data_points):
	n = len(data_points)
	x_values = [point[0] for point in data_points]
	y_values = [point[1] for point in data_points]
	sum_x = sum(x_values)
	sum_y = sum(y_values)
	sum_x_squared = sum(x ** 2 for x in x_values)
	sum_xy = sum(x * y for x, y in data_points)
	k = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
	b = (sum_y - k * sum_x) / n
	return k, b

with open("world-energy-mix-proportion.csv", "r", encoding="utf-8", newline="") as f:
	reader = csv.reader(f)
	next(reader)
	lines = [line for line in reader]

results = {}

with open("mix_fits.csv", "w+", encoding="utf-8", newline="") as f:
	writer = csv.writer(f)
	writer.writerow(["Country", "Type", "k", "b"])
	for line in lines:
		if results.get(line[0]) == None:
			results[line[0]] = {}
		data = [float(i) for i in line[42:-1]]
		points = list(zip(list(range(2010, 2023)), data))
		k, b = linear_regression(points)
		results[line[0]][line[1][0]] = {
			"k": k, "b": b
		}
		writer.writerow([line[0], line[1][0], k, b])

def trend(i):
	k = i["k"]
	b = i["b"]
	if k == 0 and b == 0:
		return "0.00"
	else:
		return "$%.4ft %s %.4g$" % (k, "+-"[b < 0], abs(b))

for country, value in results.items():
	print(" & ".join([
		country,
		trend(value["F"]),
		trend(value["N"]),
		trend(value["R"]),
	]), "\\\\")

