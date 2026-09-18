function MapFilters({ mapView, setMapView }) {
  return (
    <div className="map-filters">
      <label htmlFor="map-view">Map View</label>

      <select
        id="map-view"
        value={mapView}
        onChange={(event) => setMapView(event.target.value)}
      >
        <option>Impact Zones</option>
        <option>Traffic Congestion</option>
        <option>Evacuation Routes</option>
        <option>Construction Sites</option>
        <option>Emergency Services</option>
      </select>

      <p>Selected view: {mapView}</p>
    </div>
  );
}

export default MapFilters;