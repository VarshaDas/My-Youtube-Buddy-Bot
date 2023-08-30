import googleapiclient.discovery
import google_auth_oauthlib.flow
import requests

def fetch_comments_from_video(video_id, api_key):
    # Set up the YouTube API client
    api_service_name = "youtube"
    api_version = "v3"
    
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    # Fetch comments for the specified video
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,  # Adjust as needed
        order="time"
    )

    comments = []
    response = request.execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments


def reply_to_comment(comment_text, comment_id, developer_key, client_secrets_file):
    # Function to reply to a comment
    
    api_service_name = "youtube"
    api_version = "v3"
    
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, ["https://www.googleapis.com/auth/youtube.force-ssl"])
    credentials = flow.run_local_server(port=8080)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    reply_payload = {
        "snippet": {
            "parentId": comment_id,
            "textOriginal": comment_text
        }
    }
    
    # Make an API call to post the reply
    request = youtube.comments().insert(
        part="snippet",
        body=reply_payload
    )
    
    try:
        response = request.execute()
        print("Reply posted successfully!")
    except Exception as e:
        print("Failed to post reply.")
        print("Error:", str(e))
