import os
from youtube_api import fetch_comments_from_video, reply_to_comment
from comment_processing import filter_comments_with_no_replies

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    CLIENT_SECRETS_FILE = "client_secret_bot.json"
    DEVELOPER_KEY = ""
    VIDEO_ID = ""

    comments = fetch_comments_from_video(VIDEO_ID, DEVELOPER_KEY)
    
    comments_with_no_replies = filter_comments_with_no_replies(comments)
    
    for comment in comments_with_no_replies:
        comment_text = input(f"Enter your reply for the following comment: {comment['snippet']['topLevelComment']['snippet']['textDisplay']}\n")
        comment_id = comment['id']
        reply_to_comment(comment_text, comment_id, CLIENT_SECRETS_FILE, DEVELOPER_KEY)

if __name__ == "__main__":
    main()
