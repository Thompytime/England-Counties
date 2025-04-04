import os
import requests

def download_image(image_filename, folder="images4"):
    """Downloads an image using Wikimedia's Special:Redirect to bypass 403 errors."""
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Wikimedia Commons API URL for direct access
    image_url = f"https://commons.wikimedia.org/wiki/Special:Redirect/file/{image_filename}"

    # Add a User-Agent header to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(image_url, stream=True, headers=headers)
    if response.status_code == 200:
        # Extract the part before "_UK_locator_map_2010" and replace underscores with spaces
        county_name = image_filename.split("_UK_locator_map_2010")[0]
        # Handle "County_Durham" correctly
        if county_name == "County_Durham":
            county_name = "Durham"
        # Replace underscores with spaces
        filename = f"{county_name.replace('_', ' ')}.svg"
        
        # Save the image
        filename_path = os.path.join(folder, filename)
        with open(filename_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"✅ Downloaded: {filename_path}")
    else:
        print(f"❌ Failed to download: {image_url} (Status code: {response.status_code})")

# List of image filenames for all 48 ceremonial counties
county_image_filenames = [
    "Bedfordshire_UK_locator_map_2010.svg",
    "Berkshire_UK_locator_map_2010.svg",
    "Bristol_UK_locator_map_2010.svg",
    "Buckinghamshire_UK_locator_map_2010.svg",
    "Cambridgeshire_UK_locator_map_2010.svg",
    "Cheshire_UK_locator_map_2010.svg",
    "City_of_London_in_Greater_London.svg",
    "Cornwall_UK_locator_map_2010.svg",
    "Cumbria_UK_locator_map_2010.svg",
    "Derbyshire_UK_locator_map_2010.svg",
    "Devon_UK_locator_map_2010.svg",
    "Dorset_UK_locator_map_2010.svg",
    "County_Durham_UK_locator_map_2010.svg",
    "East_Riding_of_Yorkshire_UK_locator_map_2010.svg",
    "East_Sussex_UK_locator_map_2010.svg",
    "Essex_UK_locator_map_2010.svg",
    "Gloucestershire_UK_locator_map_2010.svg",
    "Greater_London_UK_locator_map_2010.svg",
    "Greater_Manchester_UK_locator_map_2010.svg",
    "Hampshire_UK_locator_map_2010.svg",
    "Herefordshire_UK_locator_map_2010.svg",
    "Hertfordshire_UK_locator_map_2010.svg",
    "Isle_of_Wight_UK_locator_map_2010.svg",
    "Kent_UK_locator_map_2010.svg",
    "Lancashire_UK_locator_map_2010.svg",
    "Leicestershire_UK_locator_map_2010.svg",
    "Lincolnshire_UK_locator_map_2010.svg",
    "Merseyside_UK_locator_map_2010.svg",
    "Norfolk_UK_locator_map_2010.svg",
    "North_Yorkshire_UK_locator_map_2010.svg",
    "Northamptonshire_UK_locator_map_2010.svg",
    "Northumberland_UK_locator_map_2010.svg",
    "Nottinghamshire_UK_locator_map_2010.svg",
    "Oxfordshire_UK_locator_map_2010.svg",
    "Rutland_UK_locator_map_2010.svg",
    "Shropshire_UK_locator_map_2010.svg",
    "Somerset_UK_locator_map_2010.svg",
    "South_Yorkshire_UK_locator_map_2010.svg",
    "Staffordshire_UK_locator_map_2010.svg",
    "Suffolk_UK_locator_map_2010.svg",
    "Surrey_UK_locator_map_2010.svg",
    "Tyne_and_Wear_UK_locator_map_2010.svg",
    "Warwickshire_UK_locator_map_2010.svg",
    "West_Midlands_UK_locator_map_2010.svg",
    "West_Sussex_UK_locator_map_2010.svg",
    "West_Yorkshire_UK_locator_map_2010.svg",
    "Wiltshire_UK_locator_map_2010.svg",
    "Worcestershire_UK_locator_map_2010.svg"
]

# Loop through the list and download images, saving them with county names
for image_filename in county_image_filenames:
    download_image(image_filename)
