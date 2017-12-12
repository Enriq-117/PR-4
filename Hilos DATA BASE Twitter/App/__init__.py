import threading

from tweepy import Stream, OAuthHandler, API,cursor
from tweepy.streaming import StreamListener
from tweepy.models import User
import json
import sqlite3

# db = sqlite3.connect('DB/db-tweet')
# cursor = db.cursor()
# try:
#     cursor.execute('''CREATE TABLE tweet (ID INTEGER PRIMARY KEY, TWEET TEXT)''')
#
# except Exception as e:
#     print('TABLA SUCCESS')
#     pass

ckey = 'l69u7Ad8VYyxzt6XD1EHk2xOk'
csecret = 'Gm6gBXoN141WmxJzTcVaFwImMUAdjc3TN7CPtC6S7XPV18Mz4p'
atoken = '3376706038-CdCsf31KVnV3L7EWDWquElAjGck1qf745GeXABc'
asecret ='AtyToghnoUpKSloJiw8lJAHTVJIlIkXnz6mcMuHDW4c6b'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = API(auth)

class TLListener(StreamListener):
    def on_data(self,raw_data):
        data = json.loads(raw_data)
        status = User.parse(self.api, data)
        tweet = status.text
        print(tweet)
        return (True)


    def on_error(self, status_code):
        if status_code == 420:
            return False

def crear_datos(data_h, c):
    for d in data_h:
        evt = threading.Event()
        c.put(d, evt)




try:
    twStream = Stream(auth,TLListener())
    twStream.filter(track=['#HTML'])
except Exception as e:
    print(e)
    print('Imprimio este error')
    pass