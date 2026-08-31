import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

prompt = """
Classify the sentiment of each sentence as Positive or Negative.

Example 1:
Text: I really enjoyed the movie.
Sentiment: Positive

Example 2:
Text: The food was cold and disappointing.
Sentiment: Negative

Example 3:
Text: The service was excellent and friendly.
Sentiment: Positive

Now classify this sentence:
Text: The new laptop works perfectly and I am very happy with it.
Sentiment:
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print("Response:")
print(response.text)