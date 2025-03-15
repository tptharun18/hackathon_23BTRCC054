Here's an updated version of the README with specific details for commands related to time, date, weather, and other functionalities.

# AI Assistant README

## Overview
This AI Assistant is a voice-activated virtual assistant that performs various tasks such as controlling applications, sending WhatsApp messages, providing weather updates, performing calculations, and more. It utilizes a combination of speech recognition, text-to-speech, web scraping, and external APIs to assist users with a variety of tasks.

## Features
- **Voice Recognition:** The assistant listens to and processes voice commands.
- **Text-to-Speech:** It responds to user queries through speech.
- **Weather Information:** Provides current weather and forecasts using OpenWeather API.
- **Application Control:** Opens applications like Notepad, Calculator, and websites like Netflix, YouTube, and Google.
- **WhatsApp Messaging:** Sends messages to saved contacts via WhatsApp.
- **Navigation Assistance:** Provides directions via Google Maps.
- **Public Transport Info:** Accesses public transport schedules based on the user's location.
- **Real-time News:** Fetches the latest news from Google News.
- **Mathematical Calculations:** Performs basic mathematical operations like addition, subtraction, multiplication, division, and square roots.
- **Time & Date:** Tells the current time and date.

## Libraries Used
- **speech_recognition:** For converting speech to text.
- **pyttsx3:** For converting text to speech.
- **requests:** To fetch weather data and other API calls.
- **webbrowser:** To open websites and Google Maps.
- **geocoder:** To obtain the user's location for services like weather and navigation.
- **pywhatkit:** To send WhatsApp messages instantly.
- **math:** For performing basic mathematical operations.
- **re:** To handle regular expressions for parsing commands.
- **datetime:** For handling time and date functionality.

## Working
1. **Listening for Commands:** The assistant continuously listens for user input through the microphone using the `speech_recognition` library.
2. **Processing Commands:** It processes the received voice commands, identifying keywords and phrases related to various tasks like opening apps, sending messages, or providing information.
3. **Executing Actions:** Based on the command, the assistant will either perform a calculation, open an app, fetch weather information, or carry out other actions like sending messages or navigating to a location.
4. **Response:** The assistant provides a spoken response using `pyttsx3` and also prints out relevant data in the console.

## Time and Date Commands
The AI Assistant can provide you with the current time and date. Here are the commands for those functionalities:

- **Get the Current Time:**
  - Command: "What is the time?"
  - Example Response: "The time is 03:30 PM."
  
- **Get the Current Date:**
  - Command: "What is the date today?" or "What’s the date?"
  - Example Response: "Today is Friday, March 15, 2025."

- **Custom Date Format:**
  - Command: "Tell me today's date in full format."
  - Example Response: "Today is Friday, March 15, 2025."

## Weather Commands
The assistant can provide you with current weather information or forecasts:

- **Get the Current Weather:**
  - Command: "What's the weather today?"
  - Example Response: "The temperature in New York is 15°C with light rain."

- **Get Weather Forecast:**
  - Command: "What's the weather forecast for tomorrow?" or "What’s the weather today in London?"
  - Example Response: "Weather forecast for London today: 10:00 AM: 12°C, Clear sky. 1:00 PM: 14°C, Partly cloudy."

## Navigation and Transport Commands
You can use the assistant to get navigation help or public transport information:

- **Navigate to a Location:**
  - Command: "Navigate to Times Square."
  - Example Response: "Opening Google Maps for navigation to Times Square."
  
- **Public Transport Info:**
  - Command: "What’s the public transport schedule?"
  - Example Response: "Opening public transport schedules on Google Maps."

## Application Control
The assistant can open applications and websites based on your voice commands:

- **Open an Application:**
  - Command: "Open Notepad."
  - Example Response: "Opening Notepad."

- **Open a Website:**
  - Command: "Open YouTube."
  - Example Response: "Opening YouTube."

## WhatsApp Messaging
The assistant can send WhatsApp messages to saved contacts:

- **Send a WhatsApp Message:**
  - Command: "Send message to Jane."
  - Example Response: "Okay, sending the message to Jane. What message should I send?"
  - After receiving the message: "Message sent to Jane at +91 9876543210."

## Mathematical Calculations
You can ask the assistant to perform mathematical calculations:

- **Basic Calculations:**
  - Command: "Calculate 5 plus 10."
  - Example Response: "The result is 15."

- **Square Root Calculation:**
  - Command: "What is the square root of 16?"
  - Example Response: "Square root of 16 is 4."

## Libraries Used
- **speech_recognition:** For converting speech to text.
- **pyttsx3:** For converting text to speech.
- **requests:** To fetch weather data and other API calls.
- **webbrowser:** To open websites and Google Maps.
- **geocoder:** To obtain the user's location for services like weather and navigation.
- **pywhatkit:** To send WhatsApp messages instantly.
- **math:** For performing basic mathematical operations.
- **re:** To handle regular expressions for parsing commands.
- **datetime:** For handling time and date functionality.

## Usage
1. **Run the Code:** Ensure all dependencies are installed. Then, run the script to activate the assistant.
2. **Interact with the Assistant:** Once the assistant greets you, you can issue commands like:
   - "What’s the weather today?"
   - "Send message to Alexa."
   - "Open YouTube."
   - "Calculate 5 plus 10."
   - "Navigate to Central Park."
   - "What’s the time?"

### Requirements
- Python 3.x
- Required libraries: `speech_recognition`, `pyttsx3`, `requests`, `webbrowser`, `geocoder`, `pywhatkit`, `math`, and `datetime`.
- An OpenWeather API key for weather functionality.

### Example Commands
- "What's the weather today?"
- "Open YouTube."
- "Send message to Jane."
- "Navigate to Times Square."
- "What's the time?"
- "What's the news?"
