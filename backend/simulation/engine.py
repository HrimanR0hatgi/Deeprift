def simulate_earthquake(latitude, longitude, magnitude, depth_km):

    if magnitude >= 7:
        risk_level = "HIGH"
        evacuation_priority = "IMMEDIATE"
    elif magnitude >= 5:
        risk_level = "MEDIUM"
        evacuation_priority = "HIGH"
    elif magnitude >= 3:
        risk_level = "MEDIUM"
        evacuation_priority = "MODERATE"
    else:
        risk_level = "LOW"
        evacuation_priority = "LOW"

    affected_radius_km = round(magnitude * 2, 2)

    infrastructure_damage = min(
        round((magnitude ** 2) * 0.8, 1),
        100
    )

    return {
        "disaster": "earthquake",
        "location": {
            "latitude": latitude,
            "longitude": longitude
        },
        "parameters": {
            "magnitude": magnitude,
            "depth_km": depth_km
        },
        "risk_level": risk_level,
        "affected_radius_km": affected_radius_km,
        "estimated_infrastructure_damage_percent": infrastructure_damage,
        "evacuation_priority": evacuation_priority
    }


def simulate_flood(latitude, longitude, water_depth_m, rainfall_mm):

    risk_score = min(
        round(
            water_depth_m * 25 +
            rainfall_mm * 0.1,
            1
        ),
        100
    )

    if risk_score >= 70:
        risk_level = "HIGH"
        evacuation_priority = "IMMEDIATE"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
        evacuation_priority = "HIGH"
    else:
        risk_level = "LOW"
        evacuation_priority = "MODERATE"

    affected_radius_km = round(
        max(water_depth_m * 2, rainfall_mm * 0.02),
        2
    )

    infrastructure_damage = min(
        round(risk_score * 0.8, 1),
        100
    )

    return {
        "disaster": "flood",
        "location": {
            "latitude": latitude,
            "longitude": longitude
        },
        "parameters": {
            "water_depth_m": water_depth_m,
            "rainfall_mm": rainfall_mm
        },
        "risk_level": risk_level,
        "risk_score": risk_score,
        "affected_radius_km": affected_radius_km,
        "estimated_infrastructure_damage_percent": infrastructure_damage,
        "evacuation_priority": evacuation_priority
    }


def simulate_cyclone(
    latitude,
    longitude,
    wind_speed_kmh,
    rainfall_mm,
    storm_surge_m
):

    wind_score = min((wind_speed_kmh / 200) * 60, 60)
    rainfall_score = min((rainfall_mm / 300) * 20, 20)
    surge_score = min((storm_surge_m / 5) * 20, 20)

    risk_score = round(
        wind_score + rainfall_score + surge_score,
        1
    )

    if risk_score >= 70:
        risk_level = "HIGH"
        evacuation_priority = "IMMEDIATE"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
        evacuation_priority = "HIGH"
    else:
        risk_level = "LOW"
        evacuation_priority = "MODERATE"

    affected_radius_km = round(
        wind_speed_kmh * 0.15,
        2
    )

    infrastructure_damage = min(
        round(risk_score * 0.9, 1),
        100
    )

    return {
        "disaster": "cyclone",
        "location": {
            "latitude": latitude,
            "longitude": longitude
        },
        "parameters": {
            "wind_speed_kmh": wind_speed_kmh,
            "rainfall_mm": rainfall_mm,
            "storm_surge_m": storm_surge_m
        },
        "risk_level": risk_level,
        "risk_score": risk_score,
        "affected_radius_km": affected_radius_km,
        "estimated_infrastructure_damage_percent": infrastructure_damage,
        "evacuation_priority": evacuation_priority
    }


def simulate_wildfire(
    latitude,
    longitude,
    spread_rate_kmh,
    temperature_c,
    wind_speed_kmh,
    humidity_percent
):

    risk_score = (
        spread_rate_kmh * 10
        + max(temperature_c - 20, 0) * 2
        + wind_speed_kmh * 0.5
        + max(50 - humidity_percent, 0) * 1.5
    )

    risk_score = min(round(risk_score, 1), 100)

    if risk_score >= 70:
        risk_level = "HIGH"
        evacuation_priority = "IMMEDIATE"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
        evacuation_priority = "HIGH"
    else:
        risk_level = "LOW"
        evacuation_priority = "MODERATE"

    affected_radius_km = round(
        spread_rate_kmh * 2,
        2
    )

    return {
        "disaster": "wildfire",
        "location": {
            "latitude": latitude,
            "longitude": longitude
        },
        "parameters": {
            "spread_rate_kmh": spread_rate_kmh,
            "temperature_c": temperature_c,
            "wind_speed_kmh": wind_speed_kmh,
            "humidity_percent": humidity_percent
        },
        "risk_level": risk_level,
        "risk_score": risk_score,
        "affected_radius_km": affected_radius_km,
        "evacuation_priority": evacuation_priority
    }


def run_simulation(data):

    if data.disaster == "earthquake":
        return simulate_earthquake(
            data.latitude,
            data.longitude,
            data.magnitude,
            data.depth_km
        )

    elif data.disaster == "flood":
        return simulate_flood(
            data.latitude,
            data.longitude,
            data.water_depth_m,
            data.rainfall_mm
        )

    elif data.disaster == "cyclone":
        return simulate_cyclone(
            data.latitude,
            data.longitude,
            data.wind_speed_kmh,
            data.rainfall_mm,
            data.storm_surge_m
        )

    elif data.disaster == "wildfire":
        return simulate_wildfire(
            data.latitude,
            data.longitude,
            data.spread_rate_kmh,
            data.temperature_c,
            data.wind_speed_kmh,
            data.humidity_percent
        )

    else:
        raise ValueError(f"Unsupported disaster type: {data.disaster}")