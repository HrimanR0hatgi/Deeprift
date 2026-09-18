import "./Sidebar.css";
function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-logo">
        <span>〽</span>
        <h2>DeepRift</h2>
      </div>

      <nav className="sidebar-nav">
        <a href="#home" className="active">
          🏠 <span>Home</span>
        </a>

        <a href="#simulation">
          〽 <span>Simulations</span>
        </a>

        <a href="#saved">
          🔖 <span>Saved Scenarios</span>
        </a>

        <a href="#resources">
          📄 <span>Resources</span>
        </a>

        <a href="#about">
          ⓘ <span>About</span>
        </a>
      </nav>

      <div className="sidebar-message">
        <div>🛡️</div>
        <h3>Be Prepared</h3>
        <p>
          Knowledge saves lives.
          Use this tool to understand
          risks and prepare for
          a safer tomorrow.
        </p>
      </div>
    </aside>
  );
}

export default Sidebar;