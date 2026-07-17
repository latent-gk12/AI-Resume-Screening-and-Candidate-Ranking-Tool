import streamlit as st

from utils.parser import extract_text_from_pdf
from utils.preprocessing import preprocess_text
from utils.embedding import generate_embedding
from utils.similarity import calculate_similarity
from utils.ranking import rank_candidates
from utils.export import convert_df_to_csv
from utils.pdf_report import generate_pdf

# ---------------------- PAGE CONFIG ----------------------

st.set_page_config(
    page_title="AI Resume Screening Tool",
    page_icon="📄",
    layout="wide"
)
# -------------------- INFO -------------------------------
st.info("""
### 📋 Project Summary

- 📄 AI Model: SentenceTransformer (all-MiniLM-L6-v2)
- 📑 Supports Text-based PDFs
- 🖼️ Supports Image-based PDFs (OCR)
- 📊 Ranking Method: Cosine Similarity
- 🤖 Recommendation Engine: AI Match Scoring
""")

# ---------------------- HEADER ----------------------

st.title("📄 AI Resume Screening & Candidate Ranking System")
st.markdown("---")

# ---------------------- JOB DESCRIPTION ----------------------

st.subheader("📌 Upload Job Description")

job_description = st.file_uploader(
    "Upload Job Description (.txt)",
    type=["txt"]
)

st.markdown("---")

# ---------------------- RESUMES ----------------------

st.subheader("📂 Upload Candidate Resumes")

resume_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

st.markdown("---")

# ---------------------- SCREENING ----------------------

if st.button("🚀 Start Screening"):
    with st.spinner("Analyzing resumes... Please wait."):

        if job_description is None:
            st.error("Please upload a Job Description.")

        elif len(resume_files) == 0:
            st.error("Please upload at least one Resume.")

        else:

            st.success("Files uploaded successfully!")

        # ---------------- JOB DESCRIPTION ----------------

        jd_text = job_description.read().decode("utf-8")
        jd_text = preprocess_text(jd_text)
        jd_embedding = generate_embedding(jd_text)

        # ---------------- STORE RESULTS ----------------

        candidate_results = []
        progress_bar = st.progress(0)

        total_resumes = len(resume_files)

        # ---------------- PROCESS EACH RESUME ----------------

        for index,resume in enumerate(resume_files):

            resume_text = extract_text_from_pdf(resume)

            if resume_text is None:
                st.warning(f"⚠ {resume.name} is a scanned/image-based PDF.\n" "Please upload a text-based PDF.")
                continue

            clean_text = preprocess_text(resume_text)

            resume_embedding = generate_embedding(clean_text)

            score = calculate_similarity(
                jd_embedding,
                resume_embedding
            )

            candidate_results.append(
                {
                    "Candidate Name": resume.name.replace(".pdf", ""),
                    "Match Score": round(score, 2)
                }
            )
            progress_bar.progress((index + 1)/ total_resumes)

        # ---------------- RANKING ----------------

        ranking_df = rank_candidates(candidate_results)
        best_candidate = ranking_df.iloc[0]
        st.markdown("---")
        st.subheader("🏆 Best Candidate")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Candidate",best_candidate["Candidate Name"])
        with col2:
            st.metric("Match Score",f"{best_candidate["Match Score"]:.2f}%")
        with col3:
            st.metric("Recommendation", best_candidate["Recommendation"])

        st.markdown("---")

        st.markdown("---")
        st.header("🏆 Candidate Ranking Dashboard")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("👥 Total Candidates",len(ranking_df))
        with col2:
            st.metric("🥇 Top Score",f"{ranking_df.iloc[0]['Match Score']:.2f}%")

        with col3:
            st.metric( "⭐ Best Candidate",ranking_df.iloc[0]["Candidate Name"])

        st.markdown("----")



        st.dataframe(
            ranking_df,
            use_container_width=True
        )

        csv = convert_df_to_csv(ranking_df)

        st.download_button(
            label="📥 Download Ranking Report (CSV)",
            data=csv,
            file_name="candidate_ranking_report.csv",
            mime="text/csv"
        )
        pdf_file = generate_pdf(ranking_df)

        with open(pdf_file, "rb") as pdf:
            st.download_button("📄 Download PDF Report",pdf,file_name="Candidate_Ranking_Report.pdf",mime="application/pdf")

            
st.success("✅ Resume screening completed successfully!")