import requests
import json

token = "567a284a7db50be9-2e07ee2a8caeec27-1cd69d267735c1aa"
super_admin_id = "Yajr2ynFH8iNwlt8FQjdXA=="
message_token: '6231547560582836249'

def set_web_hook():
    url = "https://chatapi.viber.com/pa/set_webhook"
    payload = {"url": "https://www.broadwayinfosys.com", "auth_token": token}
    r = requests.post(url=url, data=json.dumps(payload))
    return r.json()

obj=set_web_hook()
print(obj)


# set_web_hook()


def get_account_info():
    url = "https://chatapi.viber.com/pa/get_account_info"
    payload = {"auth_token": token}
    r = requests.post(url=url, data=json.dumps(payload))
    return r.json()
obj=get_account_info()
print(obj)


def send_text_message(text):
    url = "https://chatapi.viber.com/pa/post"
    payload = {
        "auth_token": token,
        "from": super_admin_id,
        "type": "text",
        "text": text,
    }
    r = requests.post(url=url, data=json.dumps(payload))
    print(r.json())
obj=send_text_message('''Hello
------------Today's top 10 NEWS-----------''')


def send_picture_message():
    url = "https://chatapi.viber.com/pa/post"
    payload = {
        "auth_token": token,
        "from": super_admin_id,
        "type": "picture",
        "text": "Picture description",
        "media": "https://broadwayinfosys.com/uploads/courses/31561776920552.webp",
        "thumbnail": "https://broadwayinfosys.com/uploads/courses/31561776920552.webp",
    }
    r = requests.post(url=url, data=json.dumps(payload))
    print(r.json())


# send_picture_message()


def send_contact_message():
    url = "https://chatapi.viber.com/pa/post"
    payload = {
        "auth_token": token,
        "from": super_admin_id,
        "type": "contact",
        "contact": {
            "name": "John Doe",
            "phone_number": "+12025550164",
            "image":"https://broadwayinfosys.com/uploads/courses/31561776920552.webp"
        },
    }
    r = requests.post(url=url, data=json.dumps(payload))
    print(r.json())


# send_contact_message()

#telegram_token = ""
#api_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
#chatID = "@pyhton_march_30"
#message = """
#<b>Python HTML Message</b>
#
#<i>Hello from python code</i>
#
#<b>Important:</b> Learn HTML parsing
#<u>Stay consistent and practice daily</u>
#
#• Parsing HTML
#• Extracting text
#• Working with tags
#
#<a href="https://example.com">Visit Example</a>
#"""
#response = requests.post(
#        url = api_url,
#        params={"chat_id": chatID, "text": message, "parse_mode": "HTML"},
#    )
#print(response.json())
