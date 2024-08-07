import requests
from bs4 import BeautifulSoup
from InquirerPy import inquirer
from video_downloader import record_livestream
import re

BASE_URL = 'https://live.itftennis.com'
OUTPUT_DIR = 'out'

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
        return html
    else:
        print(f"Match {match_name} not found")
        return None

def get_stream_url(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the script tag containing videoconfig
    script_tag = soup.find('script', text=re.compile(r'var videoconfig ='))
    
    if not script_tag:
        return None
    
    # Extract the JavaScript content
    script_content = script_tag.string
    
    # Use regex to find the streamUrl
    match = re.search(r'"streamUrl"\s*:\s*"([^"]+)"', script_content)
    
    if match:
        return match.group(1)
    return None

if __name__ == "__main__":
    url = BASE_URL + '/en/live-streams/'
    html = fetch_page(url)
    videos = parse_video_items(html)
    
    if not videos:
        print("No video items found.")
    else:
        match_name = select_match(videos)
        html = download_match_page(match_name, videos)
        if not html:
            print("The requested livestream page is unavailable.")

    stream_url = get_stream_url(html)
    print(stream_url)
    if stream_url:
        record_livestream(stream_url, f"{OUTPUT_DIR}/{match_name}.mp4")
    else:
        print("No stream URL found in the page.")
