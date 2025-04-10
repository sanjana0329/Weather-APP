
#  🌤️ Weather App

A Python-based weather application that provides real-time weather conditions based on the location entered by the user. The app features an attractive and user-friendly graphical interface built with **Tkinter**.


---
## 📚 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [How It Works](#how-it-works)
- [How to Run](#how-to-run)
- [Preview](#preview)
- [License](#license)
---

## Features

- Enter any location to get real-time weather conditions.
- Displays weather data like temperature, humidity, wind speed, weather description, and time zone.
- Beautiful GUI interface using **Tkinter**.
- Responsive and user-friendly design.
- Retrieves location information using **Geopy**.
- Provides accurate time and time zone information using **TimezoneFinder** and **pytz**.
- Error handling for invalid or incorrect city inputs, displaying a helpful error message.


---

## Technologies Used

- Python 3.x
- Tkinter – for building the GUI
- OpenWeatherMap API – for fetching weather data
- Requests – for API communication
- Geopy – for geocoding locations
- TimezoneFinder – for time zone information
- Pytz – for time zone conversions
- Datetime – for handling date and time

---

##  Requirements

- Python 3.x
- `requests` module
- `geopy` module
- `timezonefinder` module
- `pytz` module
- **OpenWeatherMap API Key** (free account)

### Install dependencies:

pip install requests geopy timezonefinder pytz

---

##  How It Works

It uses Geopy to geocode the location, TimezoneFinder and pytz to determine the time zone and display the current local time.
1. Launch the weather app.
2. Enter the name of the city or location in the input field.
3. Click the Search Icon button to fetch real-time weather data.
4. The app will display the current humidity, pressure, wind speed, weather description, and the local time of the location.
5. If the city is invalid or not found, an error message will appear notifying the user.
6. It uses Geopy to geocode the location, TimezoneFinder and pytz to determine the time zone and display the current local time.
---

##  How to Run

### Clone the repository:

git clone https://github.com/sanjana0329/Weather-APP.git

cd Weather-APP


### Run the script:

python password_generator.py


---

##  Preview

> _Below are screenshots of the GUI application in action:_

### 🟢 Main Interface

Main Interface

### 🟡 Weather Data Displayed

Weather Display

### 🔴 Error Message (Invalid City)

Error Message

---

##  License

This project is open-source and available under the [MIT License](LICENSE).
