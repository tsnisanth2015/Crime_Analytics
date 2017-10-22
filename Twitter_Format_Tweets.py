import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'd://DataFiles_Backup//bangalore_bk_8K.txt'

tweets_data = []
tweets_file = open(tweets_data_path,"r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print len(tweets_data)
tweets = pd.DataFrame()
tweets['Tweet_Text'] = map(lambda tweet: tweet['text'],tweets_data)
tweets['Time_Of_Tweet'] =  map(lambda tweet: tweet['created_at'],tweets_data)
tweets['Tweet_Location'] =  map(lambda tweet: tweet['place']['name'],tweets_data)
tweets['User_Native'] = map(lambda tweet: tweet['user']['location'],tweets_data)
tweets['Country'] = map(lambda tweet: tweet['place']['country'] if tweet['place']!= None else None,tweets_data)
tweets['Language'] = map(lambda tweet: tweet['lang'],tweets_data)
    
tweets.to_csv("d://DataFiles_Backup//bangalore_8k.csv", encoding='utf-8')


##tweets_by_lang = tweets['lang'].value_counts()
##
##fig, ax = plt.subplots()
##ax.tick_params(axis='x', labelsize=15)
##ax.tick_params(axis='y', labelsize=10)
##ax.set_xlabel('Languages', fontsize=15)
##ax.set_ylabel('Number of tweets' , fontsize=15)
##ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
##tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
