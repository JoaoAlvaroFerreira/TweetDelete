# TweetDelete
An automated command line tool to delete tweets.

Download the source code and unzip it. Get a Twitter Developer Account and save your credentials. Create an app for this purpose and save the following values: consumer_key","consumer_secret", "access_token","access_token_secret". Copy paste them with " on the appropriate place in the keys.json file, like so:

  "consumer_key" : "abcdefgh12345"
 
After that, open the command line on the folder you extracted the source files to. Run the following command to install required dependencies:
    
    pip install -r "requirements.txt"
   
And you're ready to go. The template for use is the following:

    python .\TweetDelete <number-of-tweets-to-delete>
    
I don't recommend doing too many at once, as to not trigger Twitter for suspicious activity. Around 3000 should be safe.

    python .\TweetDelete 3000
