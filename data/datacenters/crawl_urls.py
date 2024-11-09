import requests
from bs4 import BeautifulSoup
import csv
import tqdm

def fetch_page(page: int):
	try:
		response = requests.get(f"https://www.datacenters.com/locations?page={page}", headers={
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
		}, proxies={
			"http": "http://localhost:10809",
			"https": "http://localhost:10809"
		})
		response.raise_for_status()
	except: return None
	soup = BeautifulSoup(response.text, "html.parser")
	datacenters = soup.select(".LocationTile__location__tZKRS")
	r = []
	for datacenter in datacenters:
		r.append([
			datacenter.select_one(".LocationTile__name__NrDKr").get_text(strip=True),
			f'https://www.datacenters.com{datacenter.select_one("a").get("href")}',
		])
	return r

with open("urls.csv", "w+", newline="", encoding="utf-8") as f:
	csv.writer(f).writerow(["page", "name", "url"])

for i in tqdm.tqdm(range(1, 110)):
	page_data = None
	while not page_data:
		page_data = fetch_page(i)
	with open("urls.csv", "a", newline="", encoding="utf-8") as f:
		writer = csv.writer(f)
		for item in page_data:
			writer.writerow([i, item[0], item[1]])

