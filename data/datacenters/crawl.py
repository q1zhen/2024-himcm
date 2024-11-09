import requests
from bs4 import BeautifulSoup
import csv
import tqdm
import concurrent.futures

def fetch_page(url: str):
	try:
		response = requests.get(url, headers={
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
		}, proxies={
			"http": "http://localhost:10809",
			"https": "http://localhost:10809"
		})
		response.raise_for_status()
	except KeyboardInterrupt:
		raise
	except: return None
	soup = BeautifulSoup(response.text, "html.parser")
	def text(selector: str):
		t = soup.select_one(selector)
		return (t.get_text() if t and t.get_text().strip() else "n/a").strip()
	provider, country = soup.select_one("#relatedLocations h2").contents[0].strip().split(" Locations in ")
	return {
		"name": text("#locationName"),
		"provider": provider,
		"country": country,
		"address": text("#sidebarAddress"),
		"total_space": text("#totalSpace strong"),
		"colocation_space": text("#colocationSpace strong"),
		"total_power": text("#power strong"),
		"distance_to_airport": text("#airport strong"),
	}

props = ["name", "provider", "country", "address", "total_space", "colocation_space", "total_power", "distance_to_airport"]

with open("urls.csv", "r", newline="", encoding="utf-8") as src:
	with open("data.csv", "w+", newline="", encoding="utf-8") as f:
		csv.writer(f).writerow(["id", *props])
	reader = csv.reader(src)
	next(reader)
	lines = [line for line in reader]

def process_line(i: int, line: list):
	data = None
	while not data:
		data = fetch_page(line[2])
	row = [i, *[data[prop] for prop in props]]
	with open("data.csv", "a", newline="", encoding="utf-8") as f:
		csv.writer(f).writerow(row)

with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
	futures = [
		executor.submit(process_line, i, line)
		for i, line in enumerate(lines)
	]
	t = concurrent.futures.as_completed(futures)
	try:
		for _ in tqdm.tqdm(t, total=len(futures)): pass
	except:
		executor.shutdown(wait=False, cancel_futures=True)
