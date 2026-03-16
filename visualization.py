import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load data
df = pd.read_csv("sentiment_reviews.csv")

# 1 Bar Chart
sentiment_counts = df["Sentiment"].value_counts()

plt.figure()
sentiment_counts.plot(kind="bar")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.show()

# 2 Pie Chart
plt.figure()
sentiment_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sentiment Percentage")
plt.ylabel("")
plt.show()

# 3 Word Cloud
text = " ".join(df["Review"].astype(str))

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.title("Word Cloud of Reviews")
plt.show()

# Remove empty reviews
df = df.dropna(subset=["Review"])

# Calculate review length
df["Review_Length"] = df["Review"].astype(str).apply(len)

plt.figure()
plt.hist(df["Review_Length"], bins=20)
plt.title("Review Length Distribution")
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.show()