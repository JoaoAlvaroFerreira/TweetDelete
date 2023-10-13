# TweetDelete
An automated command line tool to delete tweets.

1. Download the source code.
2. Get a Twitter Developer Account(free) with the account you want to delete its tweets.
3. Create an app on the website for this purpose and save the following values: 
consumer_key, consumer_secret, access_token, access_token_secret.
4. Copy paste them with " on the appropriate place in the `keys.json` file, like so:

          "consumer_key" : "abcdefgh12345"
5. Download the archive of your account, This might take more than 24 hours.
6. Rename the archive to `archive.zip` and copy it to the directory of the python script.
 
After that, open the command line in the directory of the source code. Run the following command to install required dependencies:
    
    pip install -r "requirements.txt"
   
And you're ready to go. The template for use is the following:

    python ./TweetDelete <number-of-tweets-to-delete>
    
I don't recommend doing too many at once, as to not trigger Twitter for suspicious activity. Around 3000 should be safe.

    python ./TweetDelete 3000

## TODO
- Modify the script to accept terminal kill signals to do a clean before exiting.
