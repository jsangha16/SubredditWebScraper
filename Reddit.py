import praw
import pandas as pd
reddit_read_only = praw.Reddit(client_id ="mwQOUu9WJlDf4UxxwJLuxQ", client_secret="2DOX4uZ5OrjdxyYmHHQydyWIaExM0A", user_agent="university of madtown")
subreddit = reddit_read_only.subreddit("UWMadison")

posts = []
for post in subreddit.new(limit=800):
	if "CS 540" in post.title or "CS" in post.title or "CS 320" in post.title:
		posts.append(post)
		print(post.title)
		print()
posts_dict = {"Title": [], "Post Text": [], "ID": [], "Score": [], "Total Comments": [], "Post URL": []}

for p in posts:
	posts_dict["Title"].append(p.title)
	posts_dict["Post Text"].append(p.selftext)
	posts_dict["ID"].append(p.id)
	posts_dict["Score"].append(p.score)
	posts_dict["Total Comments"].append(p.num_comments)
	posts_dict["Post URL"].append(p.url)
	
cs_posts = pd.DataFrame(posts_dict)
cs_posts.to_csv("CS Posts.csv", index=True)
