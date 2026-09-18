function PopulationStats() {
  return (
    <section className="population-section">
      <div className="section-heading">
        <h2>Population Impact</h2>
        <span>Simulated Estimate</span>
      </div>

      <div className="stats-grid">
        <div className="stat-card">
          <p>Estimated Affected</p>
          <h3>12,000</h3>
          <span>People</span>
        </div>

        <div className="stat-card">
          <p>High Impact</p>
          <h3>3,500</h3>
          <span>People</span>
        </div>

        <div className="stat-card">
          <p>Medium Impact</p>
          <h3>5,000</h3>
          <span>People</span>
        </div>

        <div className="stat-card">
          <p>Low Impact</p>
          <h3>3,500</h3>
          <span>People</span>
        </div>
      </div>
    </section>
  );
}

export default PopulationStats;