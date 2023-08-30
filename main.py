import os
from youtube_api import fetch_comments_from_video, reply_to_comment
from sentiment_analysis import analyze_sentiment
from comment_processing import filter_comments_with_no_replies

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    CLIENT_SECRETS_FILE = "client_secret_bot.json"
    DEVELOPER_KEY = ""
    VIDEO_ID = "FsIyn_oe3eo"

    comments = fetch_comments_from_video(VIDEO_ID, DEVELOPER_KEY)
    
    # comments_with_no_replies = filter_comments_with_no_replies(comments)
    
    # for comment in comments_with_no_replies:
    #     comment_text = input(f"Enter your reply for the following comment: {comment['snippet']['topLevelComment']['snippet']['textDisplay']}\n")
    #     comment_id = comment['id']
    #     reply_to_comment(comment_text, comment_id, CLIENT_SECRETS_FILE, DEVELOPER_KEY)

    for i, comment in enumerate(comments):
        sentiment_score = analyze_sentiment(comment)
        print(f"Comment #{i+1}: {comment}, Sentiment Score: {sentiment_score}")




if __name__ == "__main__":
    main()
