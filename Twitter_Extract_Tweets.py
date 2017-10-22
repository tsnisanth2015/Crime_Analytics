from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time


access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

class StdOutListener(StreamListener):    
    def on_data(self, data):
        try:            
            print data
            savefile=open("d:\\bangalore.txt","a")
            savefile.write(data)
            savefile.write('\n')
            savefile.close()
            return True
        except BaseException,e:
            print 'Failed on Data',str(e)
            time.sleep(5)

    def on_error(self,status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #stream.filter(track=['murder','theft','robbery','cruelty','rape','accident','Murder','Theft','Robbery','Cruelty','Rape','Accident'])
    stream.filter(locations=[77.540558,12.906525,77.5946,12.9716])
    


