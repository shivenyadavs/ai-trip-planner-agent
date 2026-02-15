import os
from dotenv import load_dotenv
from google import genai
from tools import get_weather

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract_city(prompt):
    words = prompt.split()
    for word in words:
        if word[0].isupper():
            return word
    return "Tokyo"

def plan_trip(prompt):
    city = extract_city(prompt)
    weather_info = get_weather(city)

    final_prompt = f"""
You are a professional AI travel planner.

User request:
{prompt}

Weather Information:
{weather_info}

Provide:
1. One paragraph on cultural & historic significance
2. Current weather & forecast
3. Suggested travel dates
4. Flight options (approximate)
5. Hotel options (approximate)
6. Day-wise detailed itinerary
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=final_prompt
    )

    return response.text
