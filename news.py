import requests

from project2 import send_text_message

url = "https://www.onlinekhabar.com/wp-json/okapi/v1/trending-posts/?limit=10"


r = requests.get(url=url)
if r.status_code == 200:
   print("Successfully fetch")
   result = r.json()
   final= result['data']['news']
   for i in final:
       print("Post id:", i['post_id'])
       print("Link:", i['link'])
       print("Title:", i['title'])
       print("Published on:", i['published_date'])
       print("Post Image:", i['post_full_image'])
       send_text_message(f"Post id = {i['post_id']} Link = {i['link']} Title = {i['title']} Published Date = {i['published_date']} Post Image = {i['post_full_image']}")
else:
   print("No data")

