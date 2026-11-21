function JobMatchCard({ role, score, description }) {
  return (
    <div className="job-match-card">

      <div className="job-match-main">

        <div className="job-role-icon">
          {role.charAt(0)}
        </div>

        <div className="job-role-info">
          <h4>{role}</h4>

          <p>
            {description}
          </p>
        </div>

      </div>

      <div className="job-score">

        <strong>{score}%</strong>

        <div className="job-score-bar">
          <i
            style={{
              width: `${score}%`,
            }}
          ></i>
        </div>

        <span>match</span>

      </div>

    </div>
  );
}

export default JobMatchCard;