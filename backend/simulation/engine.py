def run_simulation(disaster, latitude, longitude, intensity):
    # Keep intensity within the expected range
    intensity = max(0, min(10, intensity))

    disaster = disaster.lower().strip()

    # Overall risk level
    if intensity < 3:
        risk_level = "LOW"
    elif intensity < 7:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"

    # Base impact score
    impact_score = round((intensity / 10) * 100, 1)

    # Disaster-specific simulation
    if disaster == "earthquake":
        affected_radius_km = round(intensity * 2, 2)
        infrastructure_damage = min(round((intensity ** 2) * 0.8, 1), 100)

        if intensity >= 8:
            evacuation_priority = "IMMEDIATE"
        elif intensity >= 5:
            evacuation_priority = "HIGH"
        elif intensity >= 3:
            evacuation_priority = "MODERATE"
        else:
            evacuation_priority = "LOW"

    elif disaster == "flood":
        affected_radius_km = round(intensity * 1.5, 2)
        infrastructure_damage = min(round((intensity ** 2) * 0.6, 1), 100)

        if intensity >= 7:
            evacuation_priority = "IMMEDIATE"
        elif intensity >= 5:
            evacuation_priority = "HIGH"
        elif intensity >= 3:
            evacuation_priority = "MODERATE"
        else:
            evacuation_priority = "LOW"

    elif disaster == "cyclone":
        affected_radius_km = round(intensity * 5, 2)
        infrastructure_damage = min(round((intensity ** 2) * 0.7, 1), 100)

        if intensity >= 8:
            evacuation_priority = "IMMEDIATE"
        elif intensity >= 6:
            evacuation_priority = "HIGH"
        elif intensity >= 3:
            evacuation_priority = "MODERATE"
        else:
            evacuation_priority = "LOW"

    elif disaster == "wildfire":
        affected_radius_km = round(intensity * 1.2, 2)
        infrastructure_damage = min(round((intensity ** 2) * 0.5, 1), 100)

        if intensity >= 8:
            evacuation_priority = "IMMEDIATE"
        elif intensity >= 6:
            evacuation_priority = "HIGH"
        elif intensity >= 3:
            evacuation_priority = "MODERATE"
        else:
            evacuation_priority = "LOW"

    else:
        # Generic fallback for unsupported disasters
        affected_radius_km = round(intensity * 2, 2)
        infrastructure_damage = min(round((intensity ** 2) * 0.7, 1), 100)

        if intensity >= 8:
            evacuation_priority = "IMMEDIATE"
        elif intensity >= 5:
            evacuation_priority = "HIGH"
        elif intensity >= 3:
            evacuation_priority = "MODERATE"
        else:
            evacuation_priority = "LOW"

    return {
        "disaster": disaster,
        "location": {
            "latitude": latitude,
            "longitude": longitude
        },
        "intensity": intensity,
        "risk_level": risk_level,
        "affected_radius_km": affected_radius_km,
        "impact_score": impact_score,
        "estimated_infrastructure_damage_percent": infrastructure_damage,
        "evacuation_priority": evacuation_priority
    }