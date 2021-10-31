'''
1. run 'pip install fbchat' on your command prompt/terminal
2. run this python script -- it will error
    a. in the error message, you will see an error on line 190 of file _state.py (revision=...)
    b. open the _state.py file and change line 190 to "revision=1" -- the current code is useless and just errors
3. run this python script again and enter your username and password when prompted
4. if you want to see more rows in the output, change the 15 in line 32 to a higher number
'''
import fbchat
import getpass

username = input("Enter Your Facebook Messenger Username: ")
password = getpass.getpass("Enter Your Facebook Messenger Password: ")
client = fbchat.Client(username, password)

allThreadsDict = {}
threadLocationTypes = ['INBOX', 'PENDING', 'ARCHIVED', 'OTHER']
for threadLocationType in threadLocationTypes:
    threadLocation = fbchat.ThreadLocation(threadLocationType)
    allThreads = client.fetchThreads(threadLocation)
    print(len(allThreads))

    for thread in allThreads:
        messageType = str(thread.type)
        if(messageType not in allThreadsDict):
            allThreadsDict[messageType] = []
        allThreadsDict[messageType].append(thread)
    
for key in allThreadsDict:
    allThreadsDict[key].sort(key=lambda x: -x.message_count)
    
print('{0:20} {1} {0:21} | {0:20} {2}'.format('', "USERS", 'GROUPS'))
print('='*99)
print('{0:34} {1} | {0:34} {1}'.format("NAME", "MESSAGE COUNT"))
for i in range(15):
    userthread = allThreadsDict['ThreadType.USER'][i]
    groupthread = allThreadsDict['ThreadType.GROUP'][i]
    print(
        f'{f"{i+1}. {userthread.name[:33]}":40} {userthread.message_count:7} | {f"{i+1}. {groupthread.name[:33]}":40} {groupthread.message_count:7}')
