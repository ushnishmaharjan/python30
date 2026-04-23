#

#
# data= {
#    "name": "suman",
#    "number1": 980,
#    "address": "nepal",
#    "surname": "testing",
#    "numbrer": 6000,
#    "age": 100,
# }
#
#
# with open ('data.json', 'w') as file:
#    json.dump(data,file,indent=4)

from typing import final

import requests

url = "https://www.onlinekhabar.com/wp-json/okapi/v1/trending-posts/?limit=3"


# r = requests.get(url=url)
# if r.status_code == 200:
#    print("Successfully fetch")
#    result = r.json()
#    final= result['data']['news']
#    for i in final:
#        print("Post id" ,i['post_id'])
#        print("Link",i['link'])
#
# else:
#    print("No data")

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

