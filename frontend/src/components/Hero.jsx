function Hero() {
  return (
    <section className="hero" id="home">
      <div className="hero-content">
        <p className="hero-tagline">DISASTER SIMULATION PLATFORM</p>

        <h2>
          Understand disasters.
          <br />
          Prepare for tomorrow.
        </h2>

        <p className="hero-description">
          Explore disaster scenarios, analyze their impact,
          and discover emergency response options.
        </p>

        <button
          className="hero-button"
          onClick={() => {
            document
              .getElementById("simulation")
              .scrollIntoView({ behavior: "smooth" });
          }}
        >
          Start Simulation →
        </button>
      </div>

      <div className="hero-icon">
        🌍
      </div>
    </section>
  );
}

export default Hero;