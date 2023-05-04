# Import Required Module
import requests
from bs4 import BeautifulSoup
 
# Web URL
Web_url = ""
 
# Get URL Content
r = requests.get(Web_url)
 
# Parse HTML Code
soup = BeautifulSoup(r.content, 'html.parser')
 
# List of all video tag
video_tags = soup.findAll('video')
print("Total ", len(video_tags), "videos found")
 
if len(video_tags) != 0:
    for video_tag in video_tags:
        video_url = video_tag.find("a")['href']
        print(video_url)
else:
    print("no videos found")
