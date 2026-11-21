function JobDescription({ value, onChange }) {
  return (
    <div className="panel job-panel">
      <div className="panel-heading">
        <div>
          <span className="panel-number">02</span>
          <h3>Target role</h3>
        </div>

        <span className="panel-label">CONTEXT</span>
      </div>

      <textarea
        value={value}
        onChange={(event) => onChange(event.target.value)}
        placeholder="Paste the job description here..."
      />

      <div className="character-count">
        {value.length} characters
      </div>
    </div>
  );
}

export default JobDescription;