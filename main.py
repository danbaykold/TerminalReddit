import praw

client_id = ""
client_secret = ""
password = ""
username = ""

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent="Terminal2Reddit v2.0.0",
    username=username)

subreddit = reddit.subreddit("python")
hot_python = subreddit.hot(limit = 5)

for submission in hot_python:
    if not submission.stickied:
        print ("Title: {}, ups: {}, downs: {}, Visited:".format(submission.title,
                                                                submission.title,
                                                                submission.title,
                                                                submission.title,
                                                                ))