from youtube_api import fetch_comments_from_video, reply_to_comment

def filter_comments_with_no_replies(comments):

    # List comments with totalReplyCount = 0
    comments_with_no_replies = [item for item in comments['items'] if item['snippet']['totalReplyCount'] == 0]
    
    return comments_with_no_replies
