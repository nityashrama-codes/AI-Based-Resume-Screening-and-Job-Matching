import { useState } from "react";

import Navbar from "./components/Navbar";
import ResumeUploader from "./components/ResumeUploader";
import JobDescription from "./components/JobDescription";
import AnalyzeButton from "./components/AnalyzeButton";
import AnalysisResult from "./components/AnalysisResult";

function App() {
  const [resumeName, setResumeName] = useState("");
  const [resumeFile, setResumeFile] = useState(null);

  const [jobDescription, setJobDescription] = useState("");

  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [showResult, setShowResult] = useState(false);

  const [analysisData, setAnalysisData] = useState(null);

  const handleResumeSelect = (event) => {
    const file = event.target.files?.[0];

    if (!file) {
      return;
    }

    setResumeName(file.name);
    setResumeFile(file);

    setShowResult(false);
    setAnalysisData(null);
  };

  const handleAnalyze = async () => {
    if (!resumeFile) {
      alert("Please upload your resume first.");
      return;
    }

    if (!jobDescription.trim()) {
      alert("Please add the job description.");
      return;
    }

    setIsAnalyzing(true);
    setShowResult(false);
    setAnalysisData(null);

    try {
      // ==========================================
      // STEP 1: Upload Resume to Backend
      // ==========================================

      const formData = new FormData();
      formData.append("file", resumeFile);

      const uploadResponse = await fetch(
        "http://127.0.0.1:8000/api/resume/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      if (!uploadResponse.ok) {
        const errorData = await uploadResponse.json().catch(() => null);

        throw new Error(
          errorData?.detail || "Resume upload failed."
        );
      }

      const uploadData = await uploadResponse.json();

      // Extracted resume text from backend
      const resumeText = uploadData.text;

      if (!resumeText) {
        throw new Error(
          "Could not extract text from the uploaded resume."
        );
      }

      // ==========================================
      // STEP 2: Send Resume + Job Description
      //         to Matching API
      // ==========================================

      const matchResponse = await fetch(
        "http://127.0.0.1:8000/api/matching/analyze",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            resume_text: resumeText,
            job_description: jobDescription,
          }),
        }
      );

      if (!matchResponse.ok) {
        const errorData = await matchResponse.json().catch(() => null);

        throw new Error(
          errorData?.detail || "Job matching failed."
        );
      }

      const matchData = await matchResponse.json();

      // ==========================================
      // STEP 3: Store Real Backend Result
      // ==========================================

      setAnalysisData(matchData);
      setShowResult(true);

    } catch (error) {
      console.error("Analysis Error:", error);

      alert(
        error.message ||
        "Something went wrong while analyzing the resume."
      );
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="app-shell">
      <div className="ambient ambient-one"></div>
      <div className="ambient ambient-two"></div>

      <Navbar />

      <main className="dashboard">

        {/* HERO */}
        <section className="hero-section">
          <div className="hero-copy">
            <span className="eyebrow">
              INTELLIGENT CAREER ANALYSIS
            </span>

            <h2>
              Understand your
              <span> job fit </span>
              before applying.
            </h2>

            <p>
              Upload a resume, describe the target role, and let
              the system identify skills, gaps and potential
              alignment.
            </p>
          </div>

          <div className="orbital-visual">
            <div className="orbit orbit-one"></div>
            <div className="orbit orbit-two"></div>
            <div className="orbit orbit-three"></div>

            <div className="core">
              <span>AI</span>
            </div>

            <div className="orbit-node node-one">
              NLP
            </div>

            <div className="orbit-node node-two">
              ML
            </div>

            <div className="orbit-node node-three">
              MATCH
            </div>
          </div>
        </section>

        {/* INPUT AREA */}
        <section className="analysis-grid">

          <ResumeUploader
            resumeName={resumeName}
            onResumeSelect={handleResumeSelect}
          />

          <JobDescription
            value={jobDescription}
            onChange={setJobDescription}
          />

        </section>

        {/* ANALYZE */}
        <AnalyzeButton
          isAnalyzing={isAnalyzing}
          onAnalyze={handleAnalyze}
        />

        {/* RESULT */}
        <AnalysisResult
          visible={showResult}
          analysisData={analysisData}
        />

      </main>
    </div>
  );
}

export default App;