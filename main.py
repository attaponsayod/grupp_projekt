from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_weather_data(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")  # Use your API key here or save it as an environment variable
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if API call was successful
        data = response.json()

        # Convert temperature from Kelvin to Celsius
        temperature_celsius = data["main"]["temp"] - 273.15

        # Create an object with the processed data
        weather_info = {
            "city": data["name"],
            "temperature": round(temperature_celsius, 1),
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None

# Function to generate HTML content with weather data table
def generate_html(weather_data):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weather Data</title>
    </head>
    <body>
        <h1>Weather Information for {weather_data['city']}</h1>
        <table border="1">
            <tr>
                <th>City</th>
                <th>Temperature (°C)</th>
                <th>Humidity (%)</th>
                <th>Description</th>
            </tr>
            <tr>
                <td>{weather_data['city']}</td>
                <td>{weather_data['temperature']}</td>
                <td>{weather_data['humidity']}</td>
                <td>{weather_data['description']}</td>
            </tr>
        </table>
    </body>
    </html>
    """
    # Write the content to an HTML file
    with open("webb_app.html", "w") as file:
        file.write(html_content)
    print("HTML file generated with weather data.")

# Test the functions
city = "Stockholm"
weather_data = get_weather_data(city)
if weather_data:
    weather_data["temperature"] = f"{weather_data['temperature']} °C"
    generate_html(weather_data)
