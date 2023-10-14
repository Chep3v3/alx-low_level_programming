import os
import requests
from bs4 import BeautifulSoup

def get_video_url_from_website(website_url):
    try:
        response = requests.get(website_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find video tags or other elements containing the video URLs
        video_tags = soup.find_all('video')  # Modify this based on the website's HTML structure

        # Extract video URLs from the video tags
        video_urls = [video['src'] for video in video_tags if 'src' in video.attrs]

        return video_urls

    except requests.RequestException as e:
        print(f"An error occurred while fetching the website content: {e}")
        return []

if __name__ == "__main__":
    website_url = "https://www.manifestedpublishers.com/course/CoLaw_IL_Class"
    video_urls = get_video_url_from_website(website_url)

    if video_urls:
        # Assuming you want to download the first video found on the website
        video_url_to_download = video_urls[0]

        # Set the save location and filename for the downloaded video
        save_location = "path/to/save/video.mp4"

        # Download the video using the previous download_video function or using youtube_dl

        # Example using the previous download_video function:
        # download_video(video_url_to_download, save_location)

        # Example using youtube_dl:
        # download_video_using_youtube_dl(video_url_to_download, save_location)
    else:
        print("No video URLs found on the website.")
