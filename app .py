import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create sentiment analyser
analyzer = SentimentIntensityAnalyzer()

# Page settings
st.set_page_config(
    page_title="MediaMood",
    page_icon="📰",
    layout="centered"
)

# Application heading
st.title("📰 MediaMood")
st.subheader("News & Social Media Sentiment Analyzer")

st.write(
    "Welcome to MediaMood! Enter any news headline, "
    "social media comment or sentence to discover its sentiment."
)

st.divider()

# Text input
user_text = st.text_area(
    "Enter your text here:",
    placeholder="Example: I really enjoyed watching this movie!",
    height=150
)

# Analyse button
if st.button("Analyse Sentiment", type="primary"):

    if user_text.strip():

        # Analyse the text
        scores = analyzer.polarity_scores(user_text)

        compound = scores["compound"]

        # Classify sentiment
        if compound >= 0.05:
            sentiment = "Positive 😊"
            st.success("The sentiment is POSITIVE")

        elif compound <= -0.05:
            sentiment = "Negative 😠"
            st.error("The sentiment is NEGATIVE")

        else:
            sentiment = "Neutral 😐"
            st.info("The sentiment is NEUTRAL")

        # Display results
        st.subheader("Analysis Result")

        st.write("**Sentiment:**", sentiment)

        st.write("**Sentiment Score:**", round(compound, 3))

        st.write("**Positive Score:**", scores["pos"])

        st.write("**Negative Score:**", scores["neg"])

        st.write("**Neutral Score:**", scores["neu"])

        st.progress((compound + 1) / 2)

        st.caption(
            "Score ranges from -1 (very negative) "
            "to +1 (very positive)."
        )

    else:
        st.warning("Please enter some text first.")

# Footer
st.divider()

st.caption("MediaMood | NLP Mini Project | Assignment 1")
st.caption("Created for educational purposes.")
