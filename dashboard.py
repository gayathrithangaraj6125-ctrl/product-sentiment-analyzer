import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("🛍️ Product Sentiment Analyzer")

st.write("Analyze customer reviews using AI sentiment analysis")

# Load dataset
df = pd.read_csv("sentiment_reviews.csv")

df = df.dropna(subset=["Review"])

# Product search
product_name = st.text_input("Enter Product Name")

if st.button("Analyze Product"):

    st.success("Analysis Started")

    # Show dataset
    st.subheader("Customer Reviews")
    st.dataframe(df.head(20))

    # Sentiment count
    sentiment_counts = df["Sentiment"].value_counts()

    st.subheader("Sentiment Distribution")

    fig1, ax1 = plt.subplots()
    sentiment_counts.plot(kind="bar", ax=ax1)
    ax1.set_xlabel("Sentiment")
    ax1.set_ylabel("Number of Reviews")

    st.pyplot(fig1)

    # Pie Chart
    st.subheader("Sentiment Percentage")

    fig2, ax2 = plt.subplots()
    sentiment_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax2)

    st.pyplot(fig2)

    # Word Cloud
    st.subheader("Word Cloud")

    text = " ".join(df["Review"].astype(str))

    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    fig3, ax3 = plt.subplots()

    ax3.imshow(wordcloud)
    ax3.axis("off")

    st.pyplot(fig3)

    # Review Length
    st.subheader("Review Length Distribution")

    df["Review_Length"] = df["Review"].astype(str).apply(len)

    fig4, ax4 = plt.subplots()

    ax4.hist(df["Review_Length"], bins=20)

    ax4.set_xlabel("Review Length")
    ax4.set_ylabel("Frequency")

    st.pyplot(fig4)

    st.success("Analysis Completed")