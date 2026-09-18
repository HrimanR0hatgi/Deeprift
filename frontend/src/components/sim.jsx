

function SimulationControls({ disaster, setDisaster, intensity, setIntensity }) {
  
  return (
    <section className="simulation" id="simulation">
      <h2>Simulation Controls</h2>

      <div className="controls">
        <label>
          Disaster Type

          <select
            value={disaster}
            onChange={(e) => setDisaster(e.target.value)}
          >
            <option>Earthquake</option>
            <option>Flood</option>
            <option>Cyclone</option>
            <option>Wildfire</option>
            <option>Tsunami</option>
          </select>
        </label>

        <label>
          Intensity: {intensity}

          <input
            type="range"
            min="1"
            max="10"
            value={intensity}
            onChange={(e) => setIntensity(Number(e.target.value))}
          />
        </label>
      </div>

      <button
        onClick={() => {
          alert(
            `Disaster: ${disaster}\nIntensity: ${intensity}`
          );
        }}
      >
        Run Simulation
      </button>
    </section>
  );
}

export default SimulationControls;