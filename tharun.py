import speech_recognition as sr
import pyttsx3
import datetime
import requests
import webbrowser
import sys
import os
import geocoder
import re
import math
import pywhatkit

# Initialize speech engine for speaking
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen for voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except Exception as e:
        print("Sorry, I couldn't understand that.")
        return None


def get_location():
    """Fetches the user's current location."""
    g = geocoder.ip('me')
    return g.city if g.city else "Unknown"


def get_weather(city, forecast=False):
    """Fetches weather data from OpenWeather API."""
    API_KEY = "YOUR-API-KEY"  # Replace with your OpenWeather API key
    endpoint = "forecast" if forecast else "weather"
    url = f"https://api.openweathermap.org/data/2.5/{endpoint}?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if forecast:
            forecasts = data['list'][:8]  # Get forecast for the next 24 hours (3-hour intervals)
            weather_report = f"Weather forecast for {city} today:\n"
            for entry in forecasts:
                time = entry['dt_txt']
                temp = entry['main']['temp']
                desc = entry['weather'][0]['description']
                weather_report += f"{time}: {temp}°C, {desc}\n"
            return weather_report
        else:
            temp = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            return f"The temperature in {city} is {temp}°C with {weather_desc}."
    else:
        return "Sorry, I couldn't fetch the weather. Please check the city name."


def open_application(command):
    """Open an application or website based on command."""
    apps = {"Notepad": "notepad.exe", "Calculator": "calc.exe"}
    sites = {"netflix": "https://www.netflix.com", "youtube": "https://www.youtube.com", "chrome": "https://www.google.com"}

    # Convert the command to lowercase for case-insensitive matching
    command_lower = command.lower()

    # Check if any of the apps or sites are mentioned in the command
    for name, path in {**apps, **sites}.items():
        if name.lower() in command_lower:  # Case-insensitive matching
            speak(f"Opening {name}.")
            if name in apps:
                os.system(path)  # Launch application
            else:
                webbrowser.open(path)  # Open website
            return
    speak("I can't open that.")



# Dictionary to store names and phone numbers
contacts = {
    "Alexa"
    "": "9880159996",  # Add other contacts here
    "Jane": "9876543210"
}


def send_whatsapp_message(command):
    """Send a WhatsApp message based on user input"""
    try:
        # Check if the command includes "send message"
        if "send message" in command:
            speak("To whom should I send the message?")
            recipient_name = listen()

            # Check if the recipient name exists in the contacts
            if recipient_name and recipient_name.capitalize() in contacts:
                phone_number = contacts[recipient_name.capitalize()]
                speak(f"Okay, sending the message to {recipient_name}. What message should I send?")
                message = listen()

                if message:
                    # Send the message using pywhatkit
                    pywhatkit.sendwhatmsg_instantly(f"+91{phone_number}", message)
                    speak(f"Message sent to {recipient_name} at {phone_number}.")
                else:
                    speak("Sorry, I couldn't understand the message.")
            else:
                speak("Sorry, I don't have that contact saved. Please check the name and try again.")
        else:
            speak("Please specify a valid command to send a message.")
    except Exception as e:
        speak(f"Error sending message: {str(e)}")
        print(f"Error: {e}")


def calculate(command):
    """Perform basic mathematical operations including square root."""
    try:
        command = command.replace("plus", "+").replace("minus", "-").replace("times", "x").replace("multiplied by", "x")
        command = command.replace("divide", "/").replace("squared", "*2").replace("cubed", "*3")

        if "square root of" in command or "sqrt" in command:
            command = re.sub(r'square root of|sqrt', '', command).strip()
            numbers = re.findall(r'\d+', command)
            if numbers:
                results = [f"Square root of {num} is {math.sqrt(float(num)):.2f}" for num in numbers]
                speak(", ".join(results))
                return

        command = re.sub(r'[^0-9+\-x/(). ]', '', command)
        command = command.replace("x", "*")
        result = eval(command)
        speak(f"The result is {result}.")
    except Exception as e:
        speak("Error performing calculation.")
        print(f"Calculation error: {e}")


def get_news():
    """Fetch and read out the top news headlines using web browser."""
    speak("Opening latest news.")
    webbrowser.open("https://news.google.com/topstories")


def get_navigation(destination):
    """Open Google Maps for navigation assistance."""
    speak(f"Opening Google Maps for navigation to {destination}.")
    webbrowser.open(f"https://www.google.com/maps/dir/?api=1&destination={destination.replace(' ', '+')}")


def get_public_transport():
    """Open Google Maps for public transport schedules."""
    speak("Opening public transport schedules on Google Maps.")
    location = geocoder.ip('me')  # Get user's current location
    lat, lon = location.latlng if location.latlng else ("28.7041", "77.1025")  # Default to Delhi if no location found
    webbrowser.open(f"https://www.google.com/maps/@{lat},{lon},14z?hl=en&mode=transit")


def process_command(command):
    """Perform actions based on voice commands."""
    if "stop" in command or "exit" in command:
        speak("Goodbye!")
        sys.exit()
    elif "time" in command and not ("times" in command or "multiplied by" in command):
        speak(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}")
    elif "date" in command:
        speak(f"Today is {datetime.datetime.today().strftime('%A, %B %d, %Y')}")
    elif "open" in command:
        open_application(command)
    elif "news" in command:
        get_news()
    elif "traffic update" in command:
        get_traffic_updates()
    elif "navigate to" in command:
        destination = command.replace("navigate to", "").strip()
        get_navigation(destination)
    elif "public transport" in command:
        get_public_transport()
    elif any(op in command for op in
             ["+", "-", "x", "/", "plus", "minus", "times", "multiplied by", "divide", "square root of", "sqrt",
              "squared", "cubed"]):
        calculate(command)
    elif "what's the weather today" in command or "weather today" in command or "weather today in" in command:
        if "in" in command:
            city = command.split("in")[-1].strip()
        else:
            city = get_location()

        weather_info = get_weather(city)  # Fetch only current weather
        print(weather_info)
        speak(weather_info)
    elif "send message to" in command:
        send_whatsapp_message(command)
    elif "open" in command:
        open_application(command)
    else:
        speak("I'm not sure how to help with that.")


if __name__ == "__main__":  # Corrected the if check
    engine = pyttsx3.init()
    speak("Hello! How can I help you today?")
    while True:
        command = listen()
        if command:
            process_command(command)
