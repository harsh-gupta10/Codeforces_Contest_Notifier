import requests
import json  # Importing the json module
from datetime import datetime, timedelta
import pytz
from twilio.rest import Client
import os


account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
from_no = os.environ.get('TWILIO_FROM_NUMBER')
to_no = os.environ.get('TWILIO_TO_NUMBER')

client = Client(account_sid, auth_token)


def get_contest_list():
    url = "https://codeforces.com/api/contest.list?gym=false"
    response = requests.get(url)
    data = response.json()
    return data





contest_list = get_contest_list()
Pending_contest = []
if contest_list["status"]=="OK":
  for item in contest_list["result"]:
    if item["phase"]=="BEFORE":
      Pending_contest.append(item)
  # contest_list["result"] = Pending_contest
else:
  ValueError("DATA cant be fetched ")


def send24HourNotification(item):
  id = item["id"]
  name = item["name"]
  type = item["type"]
  duration = int(item["durationSeconds"]/60)
  # current_time = datetime.now()
  india_timezone = pytz.timezone('Asia/Kolkata')
  current_time = datetime.now(india_timezone)
  new_time = current_time + timedelta(seconds=abs(item ["relativeTimeSeconds"]))
  formatted_date = new_time.strftime("%d-%m-%y")
  formatted_time = new_time.strftime("%H:%M")
  MsgToSend = f"Hi CP entusiast There is a contest with id:-{id} , Name:- {name} , Durations:- {duration} minutes Type:{type}.\n It is at {formatted_time} on {formatted_date}"
  message = client.messages.create(
  from_=from_no,
  body=MsgToSend,
  to=to_no
  )
  print(message.sid)


# write_to_file(contest_list, 'a.json')
for item in Pending_contest:
  if(abs(item["relativeTimeSeconds"])<150400):
    send24HourNotification(item)
