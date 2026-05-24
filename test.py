import requests
import csv
from tabulate import tabulate

header = ["iso3", "name", "unit", "buy", "sell"]
url = "https://www.nrb.org.np/api/forex/v1/rates?page=1&per_page=10&from=2025-03-01&to=2025-03-10"
while True:
    r = requests.get(url=url)
    if r.status_code == 200:
        result = r.json()["data"]["payload"]
        for i in result:
            print(i["date"])
            final_result = []
            for j in i["rates"]:

                data = [
                    j["currency"]["iso3"],
                    j["currency"]["name"],
                    j["currency"]["unit"],
                    j["buy"],
                    j["sell"],
                ]
                final_result.append(data)
            print(tabulate(final_result, header, tablefmt="grid"))
            
        pagination = r.json()["pagination"]
        if pagination.get("next") is None:
            break