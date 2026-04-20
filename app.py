from flask import Flask, render_template, request, jsonify
import folium
import pandas as pd
app = Flask(__name__)
# Load the places data from Excel
data = pd.read_excel('places.xlsx')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/map')
def map_view():
    # Create a base map centered on the world
    m = folium.Map(location=[20, 0], zoom_start=2)
    # Add markers for each type of place
    for index, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"{row['name']} (Type: {row['type']} - Area: {row['area']} acres)",
            icon=folium.Icon(color=get_marker_color(row['type']))
        ).add_to(m)
    # Save the map to an HTML file
    m.save('templates/map.html')
    return render_template('map.html')
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    results = data[data['name'].str.lower().str.contains(query)]
    return jsonify(results.to_dict(orient='records'))
@app.route('/view_type', methods=['GET'])
def view_type():
    place_type = request.args.get('type', '').lower()
    results = data[data['type'].str.lower() == place_type]
    return jsonify(results.to_dict(orient='records'))
def get_marker_color(place_type):
    colors = {
        'greenest': 'green',
        'hottest': 'red',
        'coldest': 'blue',
        'driest': 'orange',
        'wettest': 'purple',
        'cleanest': 'darkgreen',
        'dirtiest': 'darkred',
        'largest': 'darkblue',
        'smallest': 'lightblue'
    }
    return colors.get(place_type, 'gray')  # Default color if type not found
if __name__ == '__main__':
    app.run(debug=True)
