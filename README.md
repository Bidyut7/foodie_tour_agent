# 🥘 Food Tour Planner with Julep

Plan a personalized **food tour itinerary** for multiple cities by combining **weather conditions**, **local cuisines**, and **top restaurants** using the [Julep](https://julep.ai) platform with integrations like **Google Places** and **OpenWeatherMap**.

---

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [🚀 Features](#-features)
- [🔧 Prerequisites](#-prerequisites)
- [📁 Directory Structure](#-directory-structure)
- [⚙️ Setup Instructions](#-setup-instructions)
- [🧠 Workflow Explanation](#-workflow-explanation)
- [💡 Usage](#-usage)
- [📌 Sample Output](#-sample-output)
- [📞 Support](#-support)

---

## 🎯 Project Overview

This Julep-based agent automates planning a detailed **food itinerary** by:
- Fetching real-time weather for cities
- Finding popular local cuisines
- Searching best restaurants for those cuisines
- Generating an itinerary with recommendations

---

## 🚀 Features

- 🔍 Real-time **weather and place search**
- 🍜 Detects **local food specialties**
- 🍽️ Suggests **best restaurants** for indoor/outdoor dining based on weather
- 📆 Generates a **time-wise food plan** (morning, afternoon, evening)

---

## 🔧 Prerequisites

Make sure you have the following before you start:

### ✅ API Keys
| Service         | Description              | Where to Get |
|----------------|--------------------------|---------------|
| Julep           | AI Agent SDK             | [Julep.ai](https://julep.ai) |
| Google Places   | Restaurant Search        | [Google Cloud Console](https://console.cloud.google.com/apis/library/places-backend.googleapis.com) |
| OpenWeatherMap  | Weather data             | [OpenWeatherMap](https://openweathermap.org/api) |

### ✅ Tools
- Python 3.8+
- pip
- Basic terminal/command-line usage

---

## 📁 Directory Structure

food-tour-planner/
│
├── run_food_tour.py # Main script to run the planner
├── food_tour_task.yaml # Task definition for Julep agent
├── .env # Environment variables (API keys)
├── requirements.txt # Python dependencies
└── README.md # This documentation

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/food-tour-planner.git
cd food-tour-planner
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add API Keys
Create a .env file:

env
Copy
Edit
JULEP_API_KEY=your_julep_api_key
GOOGLE_API_KEY=your_google_places_api_key
OPENWEATHER_API_KEY=your_openweathermap_api_key
🧠 Workflow Explanation
The logic is defined in food_tour_task.yaml, executed via the Julep SDK.

🔄 Step-by-Step Pipeline
Input Cities:

Provided by the user: ["New York", "Paris", "Tokyo"]

Step 0 - Get Weather:

Uses OpenWeatherMap API to fetch weather for each city.

Step 1 - Get Local Cuisines:

Uses internet search to get popular local dishes.

Step 2 - Get Restaurants:

Uses Google Places API to find best-rated restaurants serving those cuisines.

Step 3 - Generate Itinerary:

Generates a smart itinerary with:

Morning / Afternoon / Evening slots

Indoor or outdoor recommendations depending on weather

Restaurant and cuisine suggestions

💡 Usage
Run the Planner:
bash
Copy
Edit
python run_food_tour.py
Make sure your .env has the correct API keys and your YAML task is named correctly.

Sample Output
makefile
Copy
Edit
Status: running
Status: succeeded
✅ Execution Succeeded:
{
  "New York": {
    "Morning": {
      "Place": "Russ & Daughters",
      "Dish": "Bagel with Lox",
      "Indoor/Outdoor": "Indoor"
    },
    ...
  },
  ...
}
📌 Notes
You can modify the locations list in run_food_tour.py to include any cities you want.

You can also enhance the logic to add cost, reviews, or even local events for full trip planning.

