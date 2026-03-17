import requests
import time

BOT_TOKEN = "8783138970:AAFixrBvnmnniDLIxM3tkcvqysmPXV3SBz4"
CHAT_ID = "8799810283"

users = ["elonmusk", "realDonaldTrump", "Cristiano"]
keywords = ["coin", "token", "crypto", "contract", "CA"]

last_data = {}

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check_user(user):
    url = f"https://nitter.net/{user}"
    r = requests.get(url)
    return r.text.lower()

while True:
    try:
        for user in users:
            data = check_user(user)

            if user not in last_data:
                last_data[user] = data
                continue

            if data != last_data[user]:
                last_data[user] = data

                if any(k in data for k in keywords):
                    send(f"🚨 {user} posted about crypto!")

        time.sleep(60)

    except Exception as e:
        print(e)
        time.sleep(30)
