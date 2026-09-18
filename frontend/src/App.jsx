import { useState } from "react";

import {
  MapContainer,
  TileLayer,
  useMapEvents,
  Polyline,
  Circle,
  Marker,
} from "react-leaflet";

import "leaflet/dist/leaflet.css";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import SimulationControls from "./components/sim";


function LocationSelector({ setLocation }) {
  useMapEvents({
    click(event) {
      const latitude = event.latlng.lat;
      const longitude = event.latlng.lng;

      console.log("Latitude:", latitude);
      console.log("Longitude:", longitude);

      setLocation({
        latitude: latitude,
        longitude: longitude,
      });
    },
  });

  return null;
}


function App() {

  const [location, setLocation] = useState(null);

  const [simulationResult, setSimulationResult] = useState(null);


  return (
    <div>

      <Navbar />

      <Hero />

      <SimulationControls
        location={location}
        setSimulationResult={setSimulationResult}
      />


      <section id="map">

        <h2>Disaster Map</h2>

        <MapContainer
          center={[12.879, 79.134]}
          zoom={13}
          style={{
            height: "500px",
            width: "100%",
          }}
        >

          <TileLayer
            attribution="&copy; OpenStreetMap contributors"
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />


          <LocationSelector
            setLocation={setLocation}
          />


          {/* Selected location marker */}

          {location && (
            <Marker
              position={[
                location.latitude,
                location.longitude,
              ]}
            />
          )}


          {/* Disaster impact radius */}

          {location &&
            simulationResult?.affected_radius_km && (
              <Circle
                center={[
                  location.latitude,
                  location.longitude,
                ]}
                radius={
                  simulationResult.affected_radius_km * 1000
                }
              />
            )}


          {/* Roads */}

          {simulationResult?.roads?.map(
            (road, index) => {

              const positions =
                road.geometry.map((point) => [
                  point.lat,
                  point.lon,
                ]);

              return (
                <Polyline
                  key={index}
                  positions={positions}
                />
              );
            }
          )}

        </MapContainer>

      </section>

    </div>
  );
}


export default App;