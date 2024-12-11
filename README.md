## This is a sample AI Agent

# Install
Requires Python 3.10+

pip install git+ssh://git@github.com/openai/swarm.git
or

pip install git+https://github.com/openai/swarm.git
# Usage
On Linux:

export OPENAI_API_KEY='API Key from OpenAI'

python weather.py

# Sample query
User: What's the weather like in Toronto now ?

Weather Agent: get_weather()

Weather Agent: The current weather in Toronto, Canada is characterized by broken clouds. The temperature is 4.09°C, and there is a wind speed of 5.81 m/s.

User: how about in Delhi

Weather Agent: get_weather()

Weather Agent: In Delhi, India, the current weather is hazy with a temperature of 12.05°C and a wind speed of 1.54 m/s.
