from textblob import TextBlob

class SupervisorAgent:
    def analyze(self, user_input, ai_response):
        sentiment = TextBlob(user_input).sentiment.polarity

        emotion = "angry" if sentiment < -0.3 else "neutral"
        confidence = 0.9

        if "not sure" in ai_response.lower() or "clarify" in ai_response.lower():
            confidence = 0.6

        return {
            "emotion": emotion,
            "confidence": confidence
        }
