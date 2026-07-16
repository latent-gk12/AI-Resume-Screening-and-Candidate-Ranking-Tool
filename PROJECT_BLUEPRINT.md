# PROJECT_BLUEPRINT.md

# Smart Resume Screening & Candidate Ranking Tool

**Status:** 🔒 Blueprint Locked (Version 1.0)

> This document is the single source of truth for Version 1.0 of the project.
> During development, only bug fixes and implementation are allowed. New ideas will be recorded under **Potential Future Enhancements** and are not part of Version 1.0.

---

# 1. Project Overview

## Problem Statement
Recruiters spend a significant amount of time manually reviewing resumes. Manual screening is repetitive, time-consuming, and may lead to inconsistent candidate evaluation.

## Proposed Solution
Build an AI-powered application that:
- Accepts one Job Description
- Accepts multiple PDF resumes
- Extracts resume content
- Compares each resume with the Job Description using NLP
- Ranks candidates by relevance
- Displays results through an intuitive dashboard
- Allows exporting ranked results

---

# 2. Objectives

- Automate initial resume screening
- Reduce manual effort
- Improve consistency in candidate ranking
- Demonstrate practical NLP techniques
- Provide a clean and easy-to-use interface

---

# 3. Target Users

### HR Recruiter
- Upload resumes
- Upload job description
- Review ranked candidates

### Hiring Manager
- Analyze shortlisted candidates
- Download ranking report

---

# 4. Project Scope

## Included
- Streamlit interface
- PDF resume upload
- Job description upload
- PDF text extraction
- Text preprocessing
- Sentence embedding generation
- Cosine similarity scoring
- Candidate ranking
- CSV export

## Not Included (Version 1.0)
- Authentication
- Database
- Email notifications
- OCR
- Cloud deployment
- AI interview assistant

---

# 5. Functional Requirements

FR-01 Upload Job Description

FR-02 Upload Multiple PDF Resumes

FR-03 Extract Resume Text

FR-04 Clean Resume Text

FR-05 Generate Embeddings

FR-06 Calculate Similarity Scores

FR-07 Rank Candidates

FR-08 Display Results

FR-09 Export CSV

---

# 6. Non-Functional Requirements

- Simple UI
- Modular architecture
- Readable code
- Fast response for normal workloads
- Easy maintenance

---

# 7. Architecture

Recruiter
↓
Upload JD + Resumes
↓
PDF Parser
↓
Text Preprocessing
↓
Embedding Generator
↓
Cosine Similarity
↓
Ranking Engine
↓
Dashboard
↓
CSV Export

---

# 8. Modules

1. app.py — User Interface

2. parser.py — PDF Text Extraction

3. preprocessing.py — Text Cleaning

4. embedding.py — Sentence Embedding Generation

5. similarity.py — Similarity Calculation

6. ranking.py — Candidate Ranking

7. export.py — CSV Export

---

# 9. Folder Structure

resume-screening/

├── app.py
├── requirements.txt
├── README.md
├── PROJECT_BLUEPRINT.md
├── uploads/
├── results/
├── assets/
├── data/
└── utils/
    ├── parser.py
    ├── preprocessing.py
    ├── embedding.py
    ├── similarity.py
    ├── ranking.py
    └── export.py

---

# 10. Data Flow

Resume PDF
→ Extract Text
→ Clean Text
→ Generate Embedding

Job Description
→ Generate Embedding

Embeddings
→ Cosine Similarity
→ Score
→ Ranking
→ Dashboard
→ CSV

---

# 11. Technology Stack

- Python
- Streamlit
- Pandas
- PyMuPDF
- sentence-transformers
- scikit-learn

---

# 12. Deliverables

- Source Code
- Streamlit Application
- PROJECT_BLUEPRINT.md
- README.md
- requirements.txt
- Sample Job Description
- Sample Resume PDFs

---

# 13. Testing Checklist

- Upload JD
- Upload one resume
- Upload multiple resumes
- Invalid PDF handling
- Empty input handling
- Correct ranking
- CSV download

---

# 14. Potential Future Enhancements

- Authentication
- SQL Database
- ATS Score
- Skill Extraction
- Resume Summarization
- LLM-based Suggestions
- Multi-language Support
- Cloud Deployment
- Recruiter Analytics Dashboard

---

# 15. Definition of Done

A release is complete when:
- All functional requirements work.
- The application runs without errors.
- Candidate ranking is generated correctly.
- CSV export works.
- Code is modular and documented.
- GitHub repository is complete.

---

# 16. Blueprint Lock

This blueprint is locked.
No new features will be added during Version 1.0 development.
Only implementation, testing, documentation, and bug fixes are permitted.