import fbchat
import datetime
import time

username = input("What is your facebook username: ")
password = input("What is your facebook password: ")

client = fbchat.Client(username, password)

topThreads = client.fetchThreads(fbchat.ThreadLocation("INBOX"), limit=20)
print("Here is a list of your 20 most recently texted chats")
for i,x in enumerate(topThreads):
    print(f"{i+1}. {x.name}")

recipientInput = input("To whom would you like to send a message (if the User/Group is listed above, you can put their corresponding number): ")
if(recipientInput.isnumeric()):
    recipientThread = topThreads[int(recipientInput)-1]
else:
    recipientThread = client.searchForThreads(recipientInput)[0]

message = input(f"What message would you like to send to {recipientThread.name}: ")

timeInput = input("At what time would you like the message to send (year-month-day-hour-minute): ")
year,month,day,hour,minute = [int(x) for x in timeInput.split('-')]

print()
print(f"Thank you for the information, your message will be sent at {hour}:{minute} on {month}/{day}/{year}")
# client.logout()

now = datetime.datetime.now()
scheduleTime = datetime.datetime(year, month, day, hour, minute)

time.sleep((scheduleTime - now).total_seconds())

client = fbchat.Client(username, password)
client.send(fbchat.Message(message), recipientThread.uid, recipientThread.type)
print("message sent!")



