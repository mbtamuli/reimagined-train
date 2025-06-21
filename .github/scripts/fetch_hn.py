#!/usr/bin/env python3
import requests

def fetch_top_hackernews(n=3):
    top_stories = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()
    news = []
    for idx, story_id in enumerate(top_stories[:n], 1):
        story = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json').json()
        title = story['title']
        url = story.get('url', f'https://news.ycombinator.com/item?id={story_id}')
        news.append(f"**{idx}. [{title}]({url})**")
    return news

if __name__ == "__main__":
    top_news = fetch_top_hackernews()
    with open('hn_top3.txt', 'w') as f:
        f.write('\n'.join(top_news))
