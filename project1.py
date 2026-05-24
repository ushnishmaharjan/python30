import requests
import mysql.connector

#db = mysql.connector.connect(host="localhost", user="root", database="python30march")

url = "https://www.nrb.org.np/api/forex/v1/rates?page=1&per_page=10&from=2025-03-01&to=2025-03-10"
while True:
    r = requests.get(url=url)
    print(r)
    if r.status_code == 200:
        result = r.json()["data"]["payload"]
        for i in result:
            date = i["date"]
            final_result = []
            for j in i["rates"]:

                iso3 = j["currency"]["iso3"]
                name = j["currency"]["name"]
                unit = j["currency"]["unit"]
                buy = j["buy"]
                sell = j["sell"]
#                insert_queiry = f"INSERT INTO exchangerate (id, date, iso3, name, unit, buy, sell) VALUES ( NULL , '{date}', '{iso3}', '{name} ', '{unit}', '{buy}', '{sell}');"
#                myterminal = db.cursor()
#                myterminal.execute(insert_queiry)
#                db.commit()

        pagination = r.json()["pagination"]
        if pagination.get("next") is None:
            break
