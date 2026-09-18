import PopulationStats from "./components/PopulationStats";
import { useState } from "react";
import {
  MapContainer,
  TileLayer,
  useMapEvents,
  Circle,
  Polyline,
  Marker,
  Popup,
} from "react-leaflet";
import "leaflet/dist/leaflet.css";

import Sidebar from "./components/sidebar";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import SimulationControls from "./components/sim";
import MapFilters from "./components/MapFilters";


function LocationSelector() {
  useMapEvents({
    click(event) {
      console.log("Latitude:", event.latlng.lat);
      console.log("Longitude:", event.latlng.lng);
    },
  });

  return null;
}

function App() {
  const [mapView, setMapView] = useState("Impact Zones");
  const [disaster, setDisaster] = useState("Earthquake");
  const [intensity, setIntensity] = useState(5);
  return (
    <div className="app-layout">
      <Sidebar />

      <main className="main-content">
        <Navbar />

        <Hero />

        <SimulationControls
  disaster={disaster}
  setDisaster={setDisaster}
  intensity={intensity}
  setIntensity={setIntensity}
/>
        <PopulationStats />
        

        <section id="map">
          <h2>Disaster Map</h2>
          <MapFilters
          mapView={mapView}
          setMapView={setMapView}
          />
          <div className="map-info">
          {mapView === "Impact Zones" && (
          <p>Showing disaster impact zones.</p>
          )}

          {mapView === "Traffic Congestion" && (
          <p>Showing traffic congestion information.</p>
          )}

          {mapView === "Evacuation Routes" && (
          <p>Showing evacuation routes.</p>
          )}

          {mapView === "Construction Sites" && (
          <p>Showing construction sites.</p>
          )}

          {mapView === "Emergency Services" && (
          <p>Showing nearby emergency services.</p>
          )}    
          </div>

          <MapContainer
            center={[12.879, 79.134]}
            zoom={13}
            style={{ height: "500px", width: "100%" }}
          >
            <TileLayer
              attribution="&copy; OpenStreetMap contributors"
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />

            <LocationSelector />

{mapView === "Impact Zones" && (
  <>
    <Circle
      center={[12.879, 79.134]}
      radius={800}
      pathOptions={{ color: "red", fillColor: "red" }}
    />

    <Circle
      center={[12.89, 79.14]}
      radius={500}
      pathOptions={{ color: "orange", fillColor: "orange" }}
    />
  </>
)}

{mapView === "Evacuation Routes" && (
  <Polyline
    positions={[
      [12.875, 79.13],
      [12.88, 79.14],
      [12.89, 79.15],
    ]}
    pathOptions={{ color: "green", weight: 6 }}
  />
)}

{mapView === "Emergency Services" && (
  <Marker position={[12.879, 79.134]}>
    <Popup>Emergency Shelter</Popup>
  </Marker>
)}
          </MapContainer>
        </section>
      </main>
    </div>
  );
}

export default App;