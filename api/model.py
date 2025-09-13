# api/model.py
from transformers import pipeline

# Load a lightweight sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

def generate_reply(text: str, lang: str = "en"):
    """
    Core AI logic for generating replies.
    - Takes user input (text + language)
    - Runs sentiment analysis
    - Returns (reply, sentiment, safety)
    """

    # If empty text
    if not text.strip():
        return "Please say something 🙂", "NEUTRAL", "SAFE"

    # Run sentiment analysis
    sentiment_result = sentiment_analyzer(text[:512])[0]
    sentiment = sentiment_result["label"]

    # Simple rule-based reply (stub — can connect to LLM later)
    if sentiment == "POSITIVE":
        reply = "I'm glad to hear that! 🌸"
    elif sentiment == "NEGATIVE":
        reply = "I'm sorry you're feeling that way. 💙 I'm here to listen."
    else:
        reply = "Thanks for sharing your thoughts."

    # Safety stub (you can integrate moderation here)
    safety = "SAFE"

    return reply, sentiment, safety
