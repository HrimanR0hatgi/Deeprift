import requests
import math


# -----------------------------
# Get nearby hospitals, fire stations and police stations
# -----------------------------

def get_nearby_services(latitude, longitude, radius):

    # -----------------------------
    # Overpass API
    # -----------------------------

    url = "https://overpass-api.de/api/interpreter"


    # -----------------------------
    # Calculate search area
    # -----------------------------

    lat_change = radius / 111
    lon_change = radius / (
        111 * math.cos(math.radians(latitude))
    )

    south = latitude - lat_change
    north = latitude + lat_change
    west = longitude - lon_change
    east = longitude + lon_change


    # -----------------------------
    # Overpass query
    # -----------------------------

    query = f"""
    [out:json];

    (
        node["amenity"="hospital"]({south},{west},{north},{east});
        node["amenity"="fire_station"]({south},{west},{north},{east});
        node["amenity"="police"]({south},{west},{north},{east});
    );

    out;
    """


    # -----------------------------
    # Send request
    # -----------------------------

    headers = {
        "User-Agent": "DisasterSimulationHackathon/1.0"
    }

    response = requests.post(
        url,
        data={"data": query},
        headers=headers,
        timeout=30
    )

    print("Status:", response.status_code)

    # Don't try to read JSON if Overpass returned an error
    if response.status_code != 200:
        print("Overpass request failed.")
        print(response.text[:500])
        return None

    data = response.json()


    # -----------------------------
    # Organize the data
    # -----------------------------

    hospitals = []
    fire_stations = []
    police_stations = []


    for place in data["elements"]:

        tags = place.get("tags", {})

        item = {
            "name": tags.get("name", "Unnamed"),
            "latitude": place["lat"],
            "longitude": place["lon"]
        }

        place_type = tags.get("amenity")

        if place_type == "hospital":
            hospitals.append(item)

        elif place_type == "fire_station":
            fire_stations.append(item)

        elif place_type == "police":
            police_stations.append(item)


    # -----------------------------
    # Final result
    # -----------------------------

    result = {
        "location": {
            "latitude": latitude,
            "longitude": longitude
        },
        "radius_km": radius,
        "hospitals": hospitals,
        "fire_stations": fire_stations,
        "police_stations": police_stations
    }

    return result


# -----------------------------
# Test the function
# -----------------------------

result = get_nearby_services(
    28.6139,
    77.2090,
    2
)


# -----------------------------
# Display results
# -----------------------------

if result is not None:

    print("\nLOCATION:")
    print(result["location"])

    print("\nRADIUS:")
    print(result["radius_km"], "km")

    print("\nHOSPITALS:")
    for hospital in result["hospitals"]:
        print(hospital)

    print("\nFIRE STATIONS:")
    for station in result["fire_stations"]:
        print(station)

    print("\nPOLICE STATIONS:")
    for station in result["police_stations"]:
        print(station)
