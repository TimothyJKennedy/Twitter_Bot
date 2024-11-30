import tweepy
import time
import random

# Tweepy API credentials
api_key = "baNcvnEXK5B1ccdZYViryHKsD"
api_secret = "mhejPMc6OToQFE8zbclg8dyFAwgSWHCTSw9o7CkUcWsT8rNv9N"
bearer_token = "AAAAAAAAAAAAAAAAAAAAABkLxQEAAAAAU%2FI19iH1kIGACeBLgsIfKc7txm4%3DAEmcywatGqkHwtMO3v61Xw7TdaintubDy1pTxQ32QkRJBSQ4X6"
access_token = "1511771539938717702-r26zFquOZoCnQGmI74W5gAswwH26sd"
access_token_secret = "jTvHglBn33s3P1ki8pbzJs9tzeNPugcnHwyd5zPbq3rqo"

# Set up Tweepy client
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# List of possible tweet texts
tweet_texts = [
    "The magic of Christmas never ends, and its greatest gifts are family and friends. 🎄❤️ #ChristmasMagic #HolidaySeason",
    "Wishing you all the warmth and wonder of Christmas! 🌟🎅🏼 #HolidayCheer #MerryChristmas",
    "The Christmas tree is up, the lights are glowing, and the holiday spirit is in full swing! 🎄✨ #ChristmasTime #FestiveSeason",
    "Don’t forget to leave some cookies for Santa tonight! 🍪🎅🏼 #SantaClaus #ChristmasEve",
    "May your Christmas be as bright as your smile and as sweet as your heart. 🎄😊 #ChristmasJoy #HolidayWishes",
    "Time to cozy up with loved ones and celebrate the most wonderful time of the year! 🎅🏼❤️ #ChristmasCozy #HolidaySeason",
    "When you stop and listen, Christmas is in every song and in every smile. 🎶❤️ #ChristmasJoy #HolidayMagic",
    "Feeling blessed to be surrounded by love this Christmas. Merry Christmas to you all! 🎄💖 #MerryChristmas #SeasonOfLove",
    "Nothing beats the magic of Christmas morning! ✨🎁 #ChristmasMorning #HolidayMagic",
    "It’s Christmas Eve! The most magical night of the year. 🎄🌟 #ChristmasEve #HolidaySeason",
    "Hoping your Christmas is wrapped in warmth, joy, and love. 🎁💖 #MerryChristmas #HolidayWishes",
    "It’s the most wonderful time of the year! Merry Christmas to all. 🎄✨ #HolidayCheer #ChristmasSpirit",
    "The best gift of all is the gift of family. Merry Christmas! 🎁👨‍👩‍👧‍👦 #FamilyChristmas #HolidayJoy",
    "Wishing you peace, love, and happiness this holiday season. 🎄💖 #ChristmasWishes #HolidaySpirit",
    "The true spirit of Christmas is love, kindness, and laughter. 🎅🏼💖 #ChristmasSpirit #SeasonOfGiving",
    "Wishing you all the best this Christmas and always! 🎄🌟 #ChristmasJoy #HolidayWishes",
    "It’s beginning to look a lot like Christmas everywhere you go! 🎅🏼🎄 #ChristmasDecor #HolidayMagic",
    "Sending you joy and warmth this holiday season. Merry Christmas! ✨🎄 #MerryChristmas #HolidaySeason",
    "May your holiday season be filled with laughter, love, and light. 🎁❤️ #ChristmasWishes #HolidayVibes",
    "Here’s to a magical Christmas and a new year full of hope and joy! 🎄✨ #NewYearHope #ChristmasMagic",
    "Let the holiday season fill your heart with love and joy. 🎅🏼💖 #HolidaySpirit #MerryChristmas",
    "Santa’s sleigh is on its way! Who’s excited for Christmas morning? 🎅🏼🎁 #ChristmasExcitement #HolidayMagic",
    "Joy to the world, it’s Christmas time! 🌍🎄 #ChristmasJoy #HolidayCheer",
    "Wishing you a Christmas as sweet as the cookies you bake. 🍪🎄 #ChristmasTreats #HolidayBaking",
    "The best memories are made during the holiday season. Merry Christmas! 🎄💖 #ChristmasMemories #HolidayJoy",
    "Here’s to a Christmas full of love, laughter, and special moments. 🎁❤️ #ChristmasJoy #HolidaySeason",
    "The Christmas countdown is on! Who’s ready for the holidays? 🎅🏼🎄 #ChristmasCountdown #HolidayVibes",
    "It’s the season of joy, laughter, and giving. Merry Christmas! 🎁✨ #SeasonOfGiving #ChristmasSpirit",
    "May the spirit of Christmas light up your heart and home. 🎄❤️ #ChristmasSpirit #HolidayWishes",
    "There’s nothing like the joy of seeing a Christmas tree lit up for the first time! 🎄✨ #ChristmasTree #HolidayMagic",
    "Spreading Christmas cheer one smile at a time! 🎅🏼😊 #ChristmasCheer #HolidayJoy",
    "Merry Christmas to all, and to all a good night! 🎄🌙 #ChristmasEve #HolidayTradition",
    "Let’s make this Christmas unforgettable with love and laughter! 🎄🎉 #ChristmasMemories #HolidayFun"
]

# Function to post a tweet
def post_tweet():
    tweet = random.choice(tweet_texts)  # Randomly select a tweet from the list
    client.create_tweet(text=tweet)     # Post the selected tweet
    print(f"Tweet posted: {tweet}")

# Run the tweet posting every hour
while True:
    post_tweet()
    time.sleep(1800)  # Sleep for 1/2 hour (1800 seconds)