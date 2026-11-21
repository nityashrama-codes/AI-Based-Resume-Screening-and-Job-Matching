import JobMatchCard from "./JobMatchCard";

function AnalysisResult({ visible, analysisData }) {
  if (!visible || !analysisData) {
    return null;
  }

  const matchAnalysis = analysisData.match_analysis || {};
  const semanticAnalysis = analysisData.semantic_analysis || {};

  const matchScore = Number(
    matchAnalysis.match_score || 0
  );

  const skillMatchScore = Number(
    matchAnalysis.skill_match_score || 0
  );

  const semanticSimilarity = Number(
    semanticAnalysis.similarity_percentage ||
    matchAnalysis.semantic_similarity ||
    0
  );

  const matchedSkills =
    matchAnalysis.matched_skills || [];

  const missingSkills =
    matchAnalysis.missing_skills || [];

  const requiredSkills =
    analysisData.required_skills || [];

  const resumeSkills =
    analysisData.resume_skills || [];

  const recommendation =
    matchAnalysis.recommendation ||
    "Analysis completed successfully.";

  const matchedCount = matchedSkills.length;
  const missingCount = missingSkills.length;

  const totalRequired =
    matchAnalysis.total_required_skills ||
    requiredSkills.length ||
    0;

  const formattedScore =
    matchScore.toFixed(0);

  const formattedSkillScore =
    skillMatchScore.toFixed(0);

  const formattedSemanticScore =
    semanticSimilarity.toFixed(0);

  return (
    <section className="results-section">

      {/* RESULT HEADER */}

      <div className="result-header">

        <div>

          <span className="eyebrow">
            ANALYSIS COMPLETE
          </span>

          <h2>
            Your compatibility snapshot
          </h2>

          <p>
            {recommendation}
          </p>

        </div>

        <div className="score-badge">

          <strong>
            {formattedScore}%
          </strong>

          <span>
            overall match
          </span>

        </div>

      </div>


      {/* MAIN METRICS */}

      <div className="result-grid">

        <MetricCard
          title="Overall job match"
          value={`${formattedScore}%`}
          progress={`${matchScore}%`}
        />

        <MetricCard
          title="Skill coverage"
          value={`${formattedSkillScore}%`}
          progress={`${skillMatchScore}%`}
        />

        <MetricCard
          title="Semantic similarity"
          value={`${formattedSemanticScore}%`}
          progress={`${semanticSimilarity}%`}
        />

      </div>


      {/* MATCHED / MISSING SKILLS */}

      <div className="skills-layout">

        <SkillCard
          title="Detected strengths"
          count={String(matchedCount).padStart(2, "0")}
          skills={matchedSkills}
          type="matched"
        />

        <SkillCard
          title="Potential gaps"
          count={String(missingCount).padStart(2, "0")}
          skills={missingSkills}
          type="missing"
        />

      </div>


      {/* RESUME SKILLS */}

      <div className="skill-card resume-skills-card">

        <div className="card-title">

          <span>
            Skills detected in resume
          </span>

          <b>
            {String(resumeSkills.length).padStart(2, "0")}
          </b>

        </div>

        <div className="skill-list">

          {resumeSkills.length > 0 ? (

            resumeSkills.map((skill) => (

              <span
                className="skill-chip matched"
                key={skill}
              >

                <i>
                  ✓
                </i>

                {skill}

              </span>

            ))

          ) : (

            <span>
              No skills detected.
            </span>

          )}

        </div>

      </div>


      {/* JOB REQUIREMENTS */}

      <div className="recommended-section">

        <div className="section-heading">

          <div>

            <span className="eyebrow">
              JOB REQUIREMENTS
            </span>

            <h3>
              Skills required for this role
            </h3>

            <p>
              Skills extracted from the job description.
            </p>

          </div>

          <span className="recommendation-count">
            {totalRequired} SKILLS
          </span>

        </div>


        <div className="job-match-list">

          {requiredSkills.length > 0 ? (

            requiredSkills.map((skill) => {

              const isMatched = matchedSkills.some(
                (matchedSkill) =>
                  matchedSkill.toLowerCase() ===
                  skill.toLowerCase()
              );

              return (
                <JobMatchCard
                  key={skill}
                  role={skill}
                  score={isMatched ? 100 : 0}
                  description={
                    isMatched
                      ? "This skill was detected in your resume."
                      : "This skill is required by the job but was not detected in your resume."
                  }
                />
              );

            })

          ) : (

            <p>
              No required skills were detected from the job description.
            </p>

          )}

        </div>

      </div>

    </section>
  );
}


function MetricCard({
  title,
  value,
  progress,
}) {

  return (

    <div className="metric-card">

      <span>
        {title}
      </span>

      <strong>
        {value}
      </strong>

      <div className="metric-line">

        <i
          style={{
            width: `${Math.min(
              Math.max(Number.parseFloat(progress) || 0,
              0),
              100
            )}%`,
          }}
        ></i>

      </div>

    </div>

  );
}


function SkillCard({
  title,
  count,
  skills,
  type,
}) {

  return (

    <div className="skill-card">

      <div className="card-title">

        <span>
          {title}
        </span>

        <b>
          {count}
        </b>

      </div>

      <div className="skill-list">

        {skills.length > 0 ? (

          skills.map((skill) => (

            <span
              className={`skill-chip ${type}`}
              key={skill}
            >

              <i>
                {type === "matched" ? "✓" : "!"}
              </i>

              {skill}

            </span>

          ))

        ) : (

          <span>
            No skills found.
          </span>

        )}

      </div>

    </div>

  );
}


export default AnalysisResult;