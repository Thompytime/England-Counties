import math
import json

def haversine_distance(lat1, lon1, lat2, lon2, unit='miles'):
    R = 3959 if unit == 'miles' else 6371  # Earth's radius in miles or kilometers
    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)
    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)
    dlat, dlon = lat2_rad - lat1_rad, lon2_rad - lon1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# County coordinates
county_coordinates = {
  "Bedfordshire": {"lat": 52.1, "lon": -0.4},
  "Berkshire": {"lat": 51.45, "lon": -0.8},
  "Bristol": {"lat": 51.45, "lon": -2.6},
  "Buckinghamshire": {"lat": 51.8, "lon": -0.75},
  "Cambridgeshire": {"lat": 52.25, "lon": 0.1},
  "Cheshire": {"lat": 53.2, "lon": -2.5},
  "City of London": {"lat": 51.515, "lon": -0.09},
  "Cornwall": {"lat": 50.4, "lon": -4.8},
  "Cumbria": {"lat": 54.5, "lon": -3.1},
  "Derbyshire": {"lat": 53.1, "lon": -1.5},
  "Devon": {"lat": 50.8, "lon": -3.8},
  "Dorset": {"lat": 50.8, "lon": -2.2},
  "Durham": {"lat": 54.77, "lon": -1.58},
  "East Riding of Yorkshire": {"lat": 53.9, "lon": -0.4},
  "East Sussex": {"lat": 50.9, "lon": 0.1},
  "Essex": {"lat": 51.75, "lon": 0.5},
  "Gloucestershire": {"lat": 51.8, "lon": -2.2},
  "Greater London": {"lat": 51.5, "lon": -0.1},
  "Greater Manchester": {"lat": 53.5, "lon": -2.3},
  "Hampshire": {"lat": 51.06, "lon": -1.3},
  "Herefordshire": {"lat": 52.05, "lon": -2.7},
  "Hertfordshire": {"lat": 51.8, "lon": -0.2},
  "Isle of Wight": {"lat": 50.6, "lon": -1.3},
  "Kent": {"lat": 51.2, "lon": 0.8},
  "Lancashire": {"lat": 53.75, "lon": -2.6},
  "Leicestershire": {"lat": 52.6, "lon": -1.1},
  "Lincolnshire": {"lat": 53.2, "lon": -0.4},
  "Merseyside": {"lat": 53.4, "lon": -3.0},
  "Norfolk": {"lat": 52.6, "lon": 1.3},
  "North Yorkshire": {"lat": 54.2, "lon": -1.5},
  "Northamptonshire": {"lat": 52.3, "lon": -0.8},
  "Northumberland": {"lat": 55.3, "lon": -2.1},
  "Nottinghamshire": {"lat": 53.0, "lon": -1.0},
  "Oxfordshire": {"lat": 51.75, "lon": -1.25},
  "Rutland": {"lat": 52.65, "lon": -0.6},
  "Shropshire": {"lat": 52.7, "lon": -2.7},
  "Somerset": {"lat": 51.1, "lon": -2.6},
  "South Yorkshire": {"lat": 53.4, "lon": -1.4},
  "Staffordshire": {"lat": 52.8, "lon": -2.0},
  "Suffolk": {"lat": 52.2, "lon": 1.3},
  "Surrey": {"lat": 51.2, "lon": -0.5},
  "Tyne and Wear": {"lat": 54.9, "lon": -1.5},
  "Warwickshire": {"lat": 52.3, "lon": -1.6},
  "West Midlands": {"lat": 52.5, "lon": -1.9},
  "West Sussex": {"lat": 50.95, "lon": -0.5},
  "West Yorkshire": { "lat": 53.8, "lon": -1.6},
  "Wiltshire": { "lat": 51.4, "lon": -1.9},
  "Worcestershire": {"lat": 52.2, "lon": -2.1}
}

def calculate_all_distances(county_coordinates):
    distances = {}
    county_names = list(county_coordinates.keys())

    for i in range(len(county_names)):
        county1 = county_names[i]
        distances[county1] = {}
        for j in range(i + 1, len(county_names)):
            county2 = county_names[j]
            lat1, lon1 = county_coordinates[county1]["lat"], county_coordinates[county1]["lon"]
            lat2, lon2 = county_coordinates[county2]["lat"], county_coordinates[county2]["lon"]

            miles = round(haversine_distance(lat1, lon1, lat2, lon2, "miles"), 2)
            kilometers = round(haversine_distance(lat1, lon1, lat2, lon2, "kilometers"), 2)

            distances[county1][county2] = {"miles": miles, "kilometers": kilometers}
            if county2 not in distances:
                distances[county2] = {}
            distances[county2][county1] = {"miles": miles, "kilometers": kilometers}

    return distances

# Calculate distances and save to JSON file
distances = calculate_all_distances(county_coordinates)

with open("distances.json", "w") as json_file:
    json.dump(distances, json_file, indent=2)

print("Distances saved to distances.json")
