from datetime import datetime
from stackapi import StackAPI

SITE = StackAPI('stackoverflow')
questions = SITE.fetch('questions', fromdate=datetime(2019, 1, 1), todate=datetime(2019, 1, 3), sort='votes')
print("QUESTIONS:")
#print(len(questions))
print(questions['items'][0])

print("-" * 50)
print("POSTS:")
posts = SITE.fetch('posts', sort='votes')
print(len(posts))
print(posts['items'][0])
print(list(posts['items'][0].keys()))
