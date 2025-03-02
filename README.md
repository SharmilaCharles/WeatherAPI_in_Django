# Weather Dashboard

A Django web application that displays weather information for cities using the OpenWeather API.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up your OpenWeather API key in settings.py
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

## Features

- Search for cities to get current weather information
- Displays temperature, feels like temperature, and weather description
- Clean and responsive interface 