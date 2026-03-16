import pandas as pd
from textblob import TextBlob

# Load scraped reviews
df = pd.read_csv("reviews.csv")

# Function to classify sentiment
def get_sentiment(text):
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(get_sentiment)

# Save new file
df.to_csv("sentiment_reviews.csv", index=False)

# Display results
print(df.head())

print("\nSentiment counts:")
print(df["Sentiment"].value_counts())