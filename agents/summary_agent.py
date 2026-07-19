from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_summary(transcript):

    prompt = f"""
You are an AI Meeting Intelligence Agent.

Analyze the meeting transcript.

Return ONLY in the following format.

SUMMARY:
<summary>

KEY POINTS:
- point1
- point2
- point3

ACTION ITEMS:
- task1
- task2
- task3

NEXT STEPS:
- next1
- next2

Transcript:
{transcript}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text