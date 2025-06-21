#!/usr/bin/env python3
import requests

def fetch_top_hackernews(n=3):
    top_stories = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()
    news = []
    for story_id in top_stories[:n]:
        story = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json').json()
        news.append(f"{story['title']} - {story.get('url', 'No URL')}\n")
    return news

if __name__ == "__main__":
    top_news = fetch_top_hackernews()
    with open('hn_top3.txt', 'w') as f:
        for item in top_news:
            f.write(item)
