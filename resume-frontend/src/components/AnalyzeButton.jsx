function AnalyzeButton({ isAnalyzing, onAnalyze }) {
  return (
    <section className="action-section">
      <button
        className="analyze-button"
        onClick={onAnalyze}
        disabled={isAnalyzing}
      >
        {isAnalyzing ? (
          <>
            <span className="loader"></span>
            Reading your profile...
          </>
        ) : (
          <>
            Analyze job fit
            <span>→</span>
          </>
        )}
      </button>

      <p>
        Your uploaded resume stays local until the analysis
        service is connected.
      </p>
    </section>
  );
}

export default AnalyzeButton;