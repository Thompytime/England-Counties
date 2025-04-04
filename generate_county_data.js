const countyCoordinates = {
    "Bedfordshire": { "lat": 52.1, "lon": -0.4 },
    "Berkshire": { "lat": 51.4, "lon": -0.8 },
    "Bristol": { "lat": 51.5, "lon": -2.6 },
    "Buckinghamshire": { "lat": 51.8, "lon": -0.8 },
    "Cambridgeshire": { "lat": 52.3, "lon": 0.1 },
    "Cheshire": { "lat": 53.2, "lon": -2.5 },
    "City of London": { "lat": 51.5, "lon": -0.1 },
    "Cornwall": { "lat": 50.4, "lon": -4.8 },
    "County Durham": { "lat": 54.8, "lon": -1.6 },
    "Cumbria": { "lat": 54.5, "lon": -3.1 },
    "Derbyshire": { "lat": 53.1, "lon": -1.5 },
    "Devon": { "lat": 50.7, "lon": -4.0 },
    "Dorset": { "lat": 50.8, "lon": -2.2 },
    "East Riding of Yorkshire": { "lat": 53.8, "lon": -0.4 },
    "East Sussex": { "lat": 50.9, "lon": 0.1 },
    "Essex": { "lat": 51.7, "lon": 0.5 },
    "Gloucestershire": { "lat": 51.9, "lon": -2.2 },
    "Greater London": { "lat": 51.5, "lon": -0.1 },
    "Greater Manchester": { "lat": 53.5, "lon": -2.3 },
    "Hampshire": { "lat": 51.0, "lon": -1.3 },
    "Herefordshire": { "lat": 52.1, "lon": -2.7 },
    "Hertfordshire": { "lat": 51.8, "lon": -0.2 },
    "Isle of Wight": { "lat": 50.7, "lon": -1.3 },
    "Kent": { "lat": 51.2, "lon": 0.7 },
    "Lancashire": { "lat": 53.8, "lon": -2.7 },
    "Leicestershire": { "lat": 52.6, "lon": -1.1 },
    "Lincolnshire": { "lat": 53.2, "lon": -0.3 },
    "Merseyside": { "lat": 53.4, "lon": -3.0 },
    "Norfolk": { "lat": 52.7, "lon": 1.1 },
    "North Yorkshire": { "lat": 54.1, "lon": -1.2 },
    "Northamptonshire": { "lat": 52.3, "lon": -0.9 },
    "Northumberland": { "lat": 55.3, "lon": -2.1 },
    "Nottinghamshire": { "lat": 53.0, "lon": -1.0 },
    "Oxfordshire": { "lat": 51.7, "lon": -1.2 },
    "Rutland": { "lat": 52.6, "lon": -0.7 },
    "Shropshire": { "lat": 52.7, "lon": -2.7 },
    "Somerset": { "lat": 51.1, "lon": -2.8 },
    "South Yorkshire": { "lat": 53.4, "lon": -1.3 },
    "Staffordshire": { "lat": 52.8, "lon": -2.0 },
    "Suffolk": { "lat": 52.2, "lon": 1.3 },
    "Surrey": { "lat": 51.2, "lon": -0.4 },
    "Tyne and Wear": { "lat": 55.0, "lon": -1.5 },
    "Warwickshire": { "lat": 52.3, "lon": -1.6 },
    "West Midlands": { "lat": 52.5, "lon": -2.0 },
    "West Sussex": { "lat": 50.9, "lon": -0.5 },
    "West Yorkshire": { "lat": 53.8, "lon": -1.6 },
    "Wiltshire": { "lat": 51.4, "lon": -2.0 },
    "Worcestershire": { "lat": 52.2, "lon": -2.2 }
};

function haversineDistance(lat1, lon1, lat2, lon2, unit = 'M') {
    const R = unit === 'M' ? 3958.8 : 6371; // Radius of Earth in miles or kilometers
    const dLat = deg2rad(lat2 - lat1);
    const dLon = deg2rad(lon2 - lon1);
    lat1 = deg2rad(lat1);
    lat2 = deg2rad(lat2);

    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(lat1) * Math.cos(lat2) *
            Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const d = R * c; // Distance in miles or kilometers
    return d;
}

function calculateBearing(lat1, lon1, lat2, lon2) {
    lat1 = deg2rad(lat1);
    lon1 = deg2rad(lon1);
    lat2 = deg2rad(lat2);
    lon2 = deg2rad(lon2);

    const y = Math.sin(lon2 - lon1) * Math.cos(lat2);
    const x = Math.cos(lat1) * Math.sin(lat2) -
            Math.sin(lat1) * Math.cos(lat2) * Math.cos(lon2 - lon1);
    let bearing = Math.atan2(y, x);
    bearing = rad2deg(bearing);
    bearing = (bearing + 360) % 360; // Normalize to 0-360 range
    return bearing;
}

function bearingToDirection(bearing) {
    const directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'];
    const index = Math.round(bearing / 45) % 8;
    return directions[index];
}

function deg2rad(deg) {
    return deg * (Math.PI / 180);
}

function rad2deg(rad) {
    return rad * (180 / Math.PI);
}

const countyData = {};

for (const county1 in countyCoordinates) {
    countyData[county1] = {};
    for (const county2 in countyCoordinates) {
        if (county1 !== county2) {
            const lat1 = countyCoordinates[county1].lat;
            const lon1 = countyCoordinates[county1].lon;
            const lat2 = countyCoordinates[county2].lat;
            const lon2 = countyCoordinates[county2].lon;

            const miles = Math.round(haversineDistance(lat1, lon1, lat2, lon2, 'M'));
            const kilometers = Math.round(haversineDistance(lat1, lon1, lat2, lon2, 'K'));
            const direction = bearingToDirection(calculateBearing(lat1, lon1, lat2, lon2));

            countyData[county1][county2] = { miles, kilometers, direction };
        }
    }
}

const jsonData = JSON.stringify(countyData, null, 4); // Convert object to JSON with indentation
const fs = require('fs'); // Node.js file system module

fs.writeFile('distances2.json', jsonData, (err) => {
    if (err) {
        console.error('Error writing to file', err);
    } else {
        console.log('distances2.json successfully written!');
    }
});