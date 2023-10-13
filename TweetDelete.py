from requests_oauthlib import OAuth1Session
from zipfile import ZipFile
import os
import json
import time
import sys


def pre_clean():
    if not os.path.exists('tweets.js'):
        with ZipFile('archive.zip', 'r') as z:
            with open('tweets.js', 'wb') as f:
                f.write(z.read('data/tweets.js')[25:])

def post_clean(tweets, number):
    tweets = tweets[number:]
    with open('tweets.js', 'w') as outfile:
        outfile.write(json.dumps(tweets , sort_keys=False, indent=2))

def loadTweets():
    with open('./tweets.js', encoding="utf8", errors="ignore") as f:
        tweets = json.load(f)
    return tweets

def printTweet(tweet):
    print("Tweet: "+ tweet['tweet']['full_text'])
    print(tweet['tweet']['retweet_count'] + ' Retweets || ' + tweet['tweet']['favorite_count'] + " Likes || Date: " + tweet['tweet']['created_at'])
    print('______________________________________________________________ \n')

def auth():

    with open('./keys.json', errors="ignore") as f:
        data = json.load(f)
    auth = data[0]
    consumer_key = auth['consumer_key']
    consumer_secret = auth['consumer_secret']
    access_token = auth['access_token']
    access_token_secret = auth['access_token_secret']
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )
    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )
    return oauth
def deleteTweet(tweet_id, oauth):

    try:
        response = oauth.post("https://api.twitter.com/1.1/statuses/destroy/"+tweet_id+".json")
    
    except response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    return response


def deleteTweets(tweets, number_to_delete, oauth):

    count = 0
    for tweet in tweets:

        printTweet(tweet)

        code = deleteTweet(tweet['tweet']['id'], oauth)

        extra = ''
        if code.status_code == 404: extra = " Deleted Already"

        print("Response code: {}".format(code.status_code) + extra)

        count = count + 1
        if(count > number_to_delete):
            break

def main():
    pre_clean()
    number_to_delete = int(sys.argv[1])
    oauth = auth()
    tweets = loadTweets()
    deleteTweets(tweets, number_to_delete, oauth)
    post_clean(tweets, number_to_delete)
    

if __name__ == '__main__':
    main()
