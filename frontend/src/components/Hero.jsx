function Hero() {
  return (
    <section className="hero" id="home">
      <p className="tagline">DISASTER SIMULATION PLATFORM</p>

      <h2>
        Understand disasters.
        <br />
        Prepare for tomorrow.
      </h2>

      <p>
        Explore disaster scenarios, analyze their impact,
        and discover emergency response options.
      </p>

      <button
        onClick={() => {
          document
            .getElementById("simulation")
            .scrollIntoView({ behavior: "smooth" });
        }}
      >
        Start Simulation
      </button>
    </section>
  );
}

export default Hero;