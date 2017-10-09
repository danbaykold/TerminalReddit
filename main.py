import praw
from colorama import Fore, Back, Style
import argparse

client_id = "PoEAOSBSTbnD4Q"
client_secret = "R-SavcQGJvBMNkSp4xvBUb26VHg"
password = "dennisisgay234"
username = "pp420420"


reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent="TerminalReddit",
    username=username)


#subreddit_visit = reddit.subreddit(subreddit)
#hot_posts = subreddit_visit.hot(limit = 5)

"""
for submission in hot_python:
    if not submission.stickied:
        print ("Title: {}, ups: {}, downs: {}, Visited:".format(submission.title,
                                                                submission.title,
                                                                submission.title,
                                                                submission.title,
                                                                ))
"""
def init_prompt():
    print "TerminalReddit v1.0.0"
    print "type \"help\" for a list of the currently suppored features/commands"
    input = raw_input("command:")
    
    subreddit()

def subreddit():
    if input == "subreddit":
        subreddit_name = raw_input("subreddit (do not include \"r/\") -->")
        subreddit_path = reddit.subreddit(subreddit_name)
        subreddit = subreddit_path.hot(limit = 50)
        if (subreddit == "exit"):
            print "exit"
        else:
            try:
                for submission in subreddit:
                    if not submission.stickied:
                        print submission.title
                        """
                        print ("Title: {}, ups: {}, downs: {}, Visited:".format(submission.title,
                                                                                submission.upvote(),
                                                                                submission.downvote(),
                                                                                submission.visited(),
                                                                                ))
                                                                                """
            except Exception:
                print "the entered subreddit was invalid"
                init_prompt()
init_prompt()