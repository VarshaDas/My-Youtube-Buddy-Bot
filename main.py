import os
import streamlit as st
from youtube_api import fetch_comments_from_video, reply_to_comment
from comment_processing import filter_comments_with_no_replies
from video_details import get_video_title
from openai_processing import generate_bot_response

# 1xSIz2JPIj4
# HpvoxRok8NQ
def main():
    # Environment and API setup
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    DEVELOPER_KEY = "AIzaSyCnAl4aZu7fgFoJZpUC2lbNCYTEmQ9odA8"

    if 'comments' not in st.session_state:
        st.session_state.comments = []
    if 'selected_ids' not in st.session_state:
        st.session_state.selected_ids = []

    # Streamlit UI setup
    st.title("YouTube Comment Bot")


    video_id = st.text_input("Enter YouTube Video URL")

    if video_id:
        st.write(f"You entered: {video_id}")

        if st.button("Fetch Comments") or st.session_state.comments:
            # Initialize session state for comments if not already done
            # Fetch and display video title
            video_title = get_video_title(video_id, DEVELOPER_KEY)
            st.write(f"Video Title: {video_title}")
            st.session_state.comments = []

            # Fetch comments
            comments = fetch_comments_from_video(video_id, DEVELOPER_KEY)

            # Filter and display comments
            st.session_state.comments = filter_comments_with_no_replies(comments)


            for comment in st.session_state.comments:
                comment_id = comment['id']
                comment_text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
                reply_needed = st.checkbox(comment_text, key=comment_id)
                if reply_needed and comment_id not in st.session_state.selected_ids:
                    st.session_state.selected_ids.append(comment_id)
                elif not reply_needed and comment_id in st.session_state.selected_ids:
                    st.session_state.selected_ids.remove(comment_id)


            # Button to process selected comment IDs
            if st.button("Process") or comment_id in st.session_state.selected_ids:
              selected_comments = [comment for comment in st.session_state.comments if comment['id'] in st.session_state.selected_ids]
              for comment in selected_comments:
                 comment_id = comment['id']
                 comment_text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
                 # Perform processing for selected comments
                 st.write(f"Processing comment ID: {comment_id}, Text: {comment_text}")
                 responsefrombot = generate_bot_response(comment_text)
                 st.write(f"responsefrombot: {responsefrombot}")

    # for comment in comments_with_no_replies:
    #     comment_text = input(f"Enter your reply for the following comment: {comment['snippet']['topLevelComment']['snippet']['textDisplay']}\n")
    #     comment_id = comment['id']
    #     reply_to_comment(comment_text, comment_id, CLIENT_SECRETS_FILE, DEVELOPER_KEY)
    #

if __name__ == "__main__":
    main()
