function Navbar() {
  return (
    <header className="topbar">
      <div className="brand">
        <div className="brand-mark">R</div>

        <div>
          <h1>ResumeOS</h1>
          <span>Resume Intelligence Studio</span>
        </div>
      </div>

      <div className="status-pill">
        <span className="status-dot"></span>
        AI engine ready
      </div>
    </header>
  );
}

export default Navbar;