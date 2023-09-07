from googleapiclient.discovery import build

def get_video_title(video_id, api_key):
    # Initialize the YouTube API client
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Fetch video details to get the title
    video_request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    video_response = video_request.execute()
    video_title = video_response['items'][0]['snippet']['title']
    return video_title
