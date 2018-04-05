import tweepy


consumer_key = "mKunLVzGKlyFYpcKtoVNIibaR"
consumer_secret = "Q1xLi6RGa9o1NoG8WsaurU2MNw7FBHu3IAlBmNkUNrq69cVmuq"
access_token = "354921961-mfT477eDRD7Q6Wd3b2IEgKMIBkNe6WlKtM3QhbLC"
access_token_secret = "gu19AxtFhoNzzD74vtZ8mrq1AHpwl1vUUvlbcc5ibCVS3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
