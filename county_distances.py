import math
import json

def haversine_distance(lat1, lon1, lat2, lon2, unit='miles'):
    """
    Calculates the great-circle distance between two points on Earth using the Haversine formula.

    Args:
        lat1: Latitude of the first point in decimal degrees.
        lon1: Longitude of the first point in decimal degrees.
        lat2: Latitude of the second point in decimal degrees.
        lon2: Longitude of the second point in decimal degrees.
        unit: 'miles' or 'kilometers' (default: 'miles').

    Returns:
        The distance between the two points in the specified unit.
    """
    R = 3959 if unit == 'miles' else 6371  # Earth's radius in miles or kilometers

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

# County coordinates (replace with your actual data)
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
    "West Yorkshire": {"lat": 53.8, "lon": -1.6},
    "Wiltshire": {"lat": 51.4, "lon": -1.9},
    "Worcestershire": {"lat": 52.2, "lon": -2.1}
}

def calculate_all_distances(county_coordinates):
    """
    Calculates the distances between all pairs of counties.

    Args:
        county_coordinates: A dictionary containing county names as keys and 
                           their coordinates (lat, lon) as values.

    Returns:
        A dictionary containing distances between each pair of counties in miles and kilometers.
    """
    distances = {}
    county_names = list(county_coordinates.keys())

    for i in range(len(county_names)):
        county1 = county_names[i]
        distances[county1] = {}
        for j in range(i + 1, len(county_names)):
            county2 = county_names[j]

            lat1 = county_coordinates[county1]["lat"]
            lon1 = county_coordinates[county1]["lon"]
            lat2 = county_coordinates[county2]["lat"]
            lon2 = county_coordinates[county2]["lon"]

            miles = haversine_distance(lat1, lon1, lat2, lon2, "miles")
            kilometers = haversine_distance(lat1, lon1, lat2, lon2, "kilometers")

            distances[county1][county2] = {"miles": round(miles, 2), "kilometers": round(kilometers, 2)}
            if county2 not in distances:
                distances[county2] = {}
            distances[county2][county1] = {"miles": round(miles, 2), "kilometers": round(kilometers, 2)}

    return distances

def generate_html_table(distances):
    """
    Generates an HTML string containing tables to display county distances.

    Args:
        distances: A dictionary containing distances between each pair of counties.

    Returns:
        An HTML string.
    """
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>County Distances</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        h1 {
            text-align: center;
        }

        .distance-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        .distance-table th, .distance-table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        .distance-table th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>County Distances</h1>
    <div id="distances-container">
    """

    for county_a in distances:
        html += f"""
        <table class="distance-table">
            <caption>Distances from {county_a}</caption>
            <thead>
                <tr>
                    <th>County</th>
                    <th>Miles</th>
                    <th>Kilometers</th>
                </tr>
            </thead>
            <tbody>
        """
        for county_b in distances[county_a]:
            html += f"""
                <tr>
                    <td>{county_b}</td>
                    <td>{distances[county_a][county_b]["miles"]}</td>
                    <td>{distances[county_a][county_b]["kilometers"]}</td>
                </tr>
            """
        html += """
            </tbody>
        </table>
        """

    html += """
    </div>
    </body>
    </html>
    """
    return html

# Calculate distances
distances = calculate_all_distances(county_coordinates)

# Generate HTML
html_output = generate_html_table(distances)

# Save the HTML to a file
with open("county_distances.html", "w") as f:
    f.write(html_output)

print("HTML file 'county_distances.html' has been generated.")