from textblob import TextBlob

# Analyze sentiment of a comment using TextBlob
def analyze_sentiment(comment):
    analysis = TextBlob(comment)
    return analysis.sentiment.polarity