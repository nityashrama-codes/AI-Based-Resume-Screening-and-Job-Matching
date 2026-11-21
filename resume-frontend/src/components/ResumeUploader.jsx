function ResumeUploader({ resumeName, onResumeSelect }) {
  return (
    <div className="panel upload-panel">

      <div className="panel-heading">

        <div>
          <span className="panel-number">01</span>

          <h3>
            Resume signal
          </h3>
        </div>

        <span className="panel-label">
          INPUT
        </span>

      </div>


      <label className="upload-zone">

        <input
          type="file"
          accept=".pdf,.docx"
          onChange={onResumeSelect}
        />


        <div className="upload-icon">
          ↑
        </div>


        {resumeName ? (
          <>
            <strong>
              {resumeName}
            </strong>

            <small>
              Resume loaded successfully
            </small>
          </>
        ) : (
          <>
            <strong>
              Drop your resume here
            </strong>

            <small>
              PDF or DOCX · up to 10 MB
            </small>
          </>
        )}

      </label>

    </div>
  );
}

export default ResumeUploader;