from textblob import TextBlob as tb #modulo para tokenizar palavras
import tweepy #API do twitter
import numpy as np

#regstro dos tokens para login na API(twitter)
consumer_key = 
consumer_secret = 

access_token = 
access_token_secret = 

#Acessao à API(twitter)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#chamando API
api = tweepy.API(auth)

#procura tweets
public_tweets = api.search('NFL')

#registrando a variável com "none" para usar depois
anl = None 

#Loop para cada tweet e sentimento identificado
tweets = []
for tweet in public_tweets:
    print(tweet.text) #imprime o texto dos tweets
    anl = tb(tweet.text)#analisa o sentimento do tweet
    print(anl.sentiment)#imprime o sentimento identificado e o subject(o quanto de opinião existe no tweet)
    polarity = analysis.sentiment.polarity
    tweets.append(polarity)#acumula a polaridade(sentimentos) dos tweets
       
#Imprime a média dos tweets analisados
print('SENTIMENT AVERAGE: ' + str(np.mean(tweets)))
