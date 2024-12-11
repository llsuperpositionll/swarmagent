import json
import requests
from swarm import Agent
from swarm.repl import run_demo_loop

WEATHER_API_KEY = 'Enter the Free API Key from openweathermap.org'

def get_weather(location, time="now"):
    """Get the current weather in a given location using OpenWeatherMap API.
    Location MUST be a city.
    """
    API_KEY = '12345'  # Replace with your actual API key
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"

    try:
        response = requests.get(URL)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                "location": data['name'],
                "country": data['sys']['country'],
                "temperature": data['main']['temp'],
                "description": data['weather'][0]['description'],
                "wind_speed": data['wind']['speed'],
                "time": time
            }
            return json.dumps(weather_info)
        else:
            error_info = {
                "error": data.get("message", "Unable to fetch weather details"),
                "location": location
            }
            return json.dumps(error_info)
                  else:
            error_info = {
                "error": data.get("message", "Unable to fetch weather details"),
                "location": location
            }
            return json.dumps(error_info)
    except Exception as e:
        return json.dumps({"error": str(e), "location": location})

def send_email(recipient, subject, body):
    print("Sending email...")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    return "Sent!"


weather_agent = Agent(
    model="gpt-4o-mini",
    name="Weather Agent",
    instructions="You are a helpful agent. Please project accurate weather information.",
    functions=[get_weather, send_email],
)

if __name__ == "__main__":
    run_demo_loop(weather_agent, stream=True)
                                                              
