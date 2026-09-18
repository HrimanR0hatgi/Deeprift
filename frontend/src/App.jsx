import { MapContainer, TileLayer, useMapEvents } from "react-leaflet";
import "leaflet/dist/leaflet.css";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import SimulationControls from "./components/sim";

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
  return (
    <div>
      <Navbar />

      <Hero />

      <SimulationControls />

      <section id="map">
        <h2>Disaster Map</h2>

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
        </MapContainer>
      </section>
    </div>
  );
}

export default App;