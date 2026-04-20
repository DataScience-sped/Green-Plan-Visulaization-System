# 🌍Green Place Visualization System (Flask + Folium)

## 📌 Overview
This project is a web-based application that visualizes different types of places around the world on an interactive map. It allows users to search for locations, filter them by category, and view them geographically using a dynamic map.

The system integrates **Flask (backend)**, **Folium (map visualization)**, and **HTML/JavaScript (frontend)** to provide an interactive user experience.

## 🎯 Features
* 🌎 Interactive world map visualization
* 🔍 Search functionality for places
* 🏷️ Filter places by category (greenest, hottest, coldest, etc.)
* 📍 Dynamic markers with detailed popups
* 🎨 Color-coded markers based on place type
* ⚡ REST API endpoints for data retrieval

## 🛠️ Technologies Used
* Python
* Flask
* Folium
* Pandas
* HTML
* CSS
* JavaScript

## 📂 Project Structure
```
├── app.py                 # Main Flask application
├── places.xlsx
├── README.md
├── templates/
    ├── index.html         # Homepage with search & filters
    ├── map.html           # Generated map file             
```

## ⚙️ How It Works
1. ## 📊 Dataset Fields
- Name
- Area (in acres)
- Latitude
- Longitude
- Type (e.g., greenest, hottest, coldest)
2. Flask Backend:
   * `/` → Loads homepage
   * `/map` → Generates and displays map using Folium
   * `/search` → Returns search results (API)
   * `/view_type` → Filters places by type (API)
3. Map Generation:
   * Markers are added dynamically
   * Colors represent different categories
   * Popups display place details
4. Frontend:
   * Users can search places
   * Filter by type using buttons
   * View results instantly without reloading

## 🚀 How to Run the Project
1. Install dependencies:
   ```bash
   pip install flask folium pandas openpyxl
   ```
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open browser:
   ```
   http://127.0.0.1:5000/
   ```

## 📊 Output
* Interactive map displaying:
  * Different places worldwide
  * Color-coded markers
  * Popups with place details
* Search results displayed dynamically
* Filtered results based on selected category

## 💡 Use Cases
* Geographic data visualization
* Environmental data analysis
* Travel and location-based applications
* Data analytics portfolio project

## 🔮 Future Improvements
* Add real-time API data
* Improve UI with dashboards (charts/graphs)
* Add user authentication
* Deploy on cloud (Heroku/AWS)
* Add clustering for better visualization
