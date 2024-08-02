import requests
from bs4 import BeautifulSoup
from InquirerPy import inquirer

BASE_URL = 'https://live.itftennis.com'

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_video_items(html):
    soup = BeautifulSoup(html, 'html.parser')
    video_items = soup.select('.video_item')
    
    videos = []
    for item in video_items:
        link_tag = item.select_one('div.video_desc_wrapper > h4 > a')
        match_name_tag = link_tag.select_one('span:nth-child(2)')
        
        if link_tag and match_name_tag:
            src = link_tag['href']
            match_name = match_name_tag.text.strip()
            videos.append((match_name, src))
    
    return videos

def select_match(videos):
    selected_match = inquirer.select(
        message="Select a match to download the page:",
        choices=[match_name for match_name, _ in videos],
    ).execute()
    return selected_match

def download_match_page(match_name, videos):
    selected_video = next((video for video in videos if video[0] == match_name), None)
    if selected_video:
        src = BASE_URL + selected_video[1]
        html = fetch_page(src)
        filename = f"out/{match_name.replace(' ', '_')}.html"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html)
        print(f"Downloaded {src} to {filename}")
    else:
        print(f"Match {match_name} not found")

if __name__ == "__main__":
    url = BASE_URL + '/en/live-streams/'
    html = fetch_page(url)
    videos = parse_video_items(html)
    
    if not videos:
        print("No video items found.")
    else:
        match_name = select_match(videos)
        download_match_page(match_name, videos)
