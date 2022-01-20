import os
import tweepy
from dotenv import load_dotenv

load_dotenv('.env')


def Api():

    api_key = os.environ.get("API_KEY")
    api_key_secret = os.environ.get("API_KEY_SECRET")
    bearer_token = os.environ.get("BEARER_TOKEN")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
    client_key = os.environ.get("CLIENT_KEY")
    client_secret = os.environ.get("CLIENT_SECRET")

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api

def timeline():
    api = Api()
    timeline = api.home_timeline()
    print("Timeline:\n")
    for tweet in timeline:
        print("{} \n{}\n\n".format(tweet.user.name, tweet.text))

def trendingTopics():
    api = Api()
    trending_topics = api.trends_place(1)
    for topic in trending_topics:
        print(topic)

def directMessage(user, text):
    api = Api()
    api.send_direct_message(user, text)

def followers():
    api = Api()
    followers = api.followers()
    for follower in followers:
        print("{} - {} - {}".format(follower.id, follower.name, follower.screen_name))

def tweetWellcome():

    confirm = input("Do you want to post a tweet? (y/n) ")
    if confirm == "y":
        api = Api()
        api.update_status("Hello, world! I'm tweeting with #Python #API #Tweepy #Twitter")
    else:
        print("Ok, bye!")

def whatsOnYourMind():
    text = input("What's on your mind? ")

    confirm = input("Do you want to post a tweet? (y/n) ")
    if confirm == "y":
        tweet(text)
    else:
        print("Ok, bye!")

def tweet(text):
    api = Api()
    api.update_status(text)

def main():
    while True:
        print("1 - What's on your mind?")
        print("2 - Timeline")
        print("3 - Trending Topics")
        print("4 - Direct Message")
        print("5 - Wellcome")
        print("6 - Followers")
        print("0 - Exit")



        option = int(input("Choose an option: "))
        
        if option == 1:
            whatsOnYourMind()
        elif option == 2:
            timeline()
        elif option == 3:
            trendingTopics()
        elif option == 4:
            user = input("Who do you want to send a message? ")
            text = input("What's on your mind? ")
            directMessage(user, text)
        elif option == 5:
            tweetWellcome()
        elif option == 6:
            followers()
        elif option == 0:
            break

if __name__ == "__main__":
    main()
