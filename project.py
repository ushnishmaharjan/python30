import mysql.connector
import json
import requests

from project2 import send_text_message

db = mysql.connector.connect(host="localhost", user="root", database="python30march")
myterminal = db.cursor()

from_date=input("Enter start date y-m-d:")
to_date=input("Enter end date y-m-d:")
url = f"https://www.nrb.org.np/api/forex/v1/rates?page=1&per_page=5&from={from_date}&to={to_date}"
while True:
    r = requests.get(url=url)
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
                insert_query = f"INSERT INTO `currency exchangerate` (date, iso3, name, unit, buy, sell) VALUES ('{date}', '{iso3}', '{name}', '{unit}', '{buy}', '{sell}')"
                myterminal.execute(insert_query)
                db.commit()

                result = (
                   f"Date = {date} Iso3 = {iso3}, name={name}, buy={buy}, sell={sell}"
                )
                send_text_message(result)

        pagination = r.json()["pagination"]
        if pagination.get("next") is None:
            break
        url = pagination.get("next")
    else:
        break
