# AI Resume Screening & Candidate Ranking System

## Overview

The **AI Resume Screening & Candidate Ranking System** is an AI-powered recruitment application that automates the initial resume screening process. It compares multiple resumes against a job description using Natural Language Processing (NLP) and semantic similarity techniques to rank candidates according to their relevance.

The application supports both **text-based** and **scanned/image-based** PDF resumes through a hybrid parsing approach. Text is extracted using **PyMuPDF**, while scanned documents are automatically processed using **Tesseract OCR**.

The project is built using a modular architecture, making it easy to maintain and extend with future features such as ATS scoring, skill extraction, authentication, database integration, and cloud deployment.

---

# Problem Statement

Recruiters often spend significant time manually reviewing resumes for every job opening. Manual screening is repetitive, time-consuming, and may lead to inconsistent candidate evaluation.

Most traditional resume screening systems rely heavily on keyword matching, which can overlook qualified candidates if different terminology is used. Additionally, many lightweight resume parsers cannot process scanned resumes.

This project addresses these limitations by using semantic AI models and OCR support to provide a more reliable and automated resume screening workflow.

---

# Project Objectives

The primary objectives of this project are:

- Automate the initial resume screening process.
- Reduce manual effort for recruiters.
- Rank candidates based on semantic similarity.
- Support both digital and scanned PDF resumes.
- Provide an interactive dashboard for recruiters.
- Generate downloadable ranking reports.
- Demonstrate the practical use of NLP in recruitment.

---

# Key Features

The current version of the application provides:

- Upload Job Description (.txt)
- Upload Multiple Resume PDFs
- Hybrid PDF Parsing (PyMuPDF + OCR)
- Automatic OCR Detection
- Resume Text Preprocessing
- SentenceTransformer Embedding Generation
- Cosine Similarity Matching
- Candidate Ranking
- Recommendation Labels
- Dashboard Metrics
- Best Candidate Summary
- Progress Indicator
- CSV Report Export
- PDF Report Export

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| User Interface | Streamlit |
| NLP Model | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Similarity Metric | Cosine Similarity |
| OCR Engine | Tesseract OCR |
| PDF Parsing | PyMuPDF |
| Image Processing | Pillow |
| PDF Image Conversion | pdf2image |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Deep Learning Backend | PyTorch |
| Report Generation | ReportLab |
| Version Control | Git & GitHub |

---

# High-Level System Architecture

```text
Recruiter
     │
     ▼
Upload Job Description + Resumes
     │
     ▼
Hybrid PDF Parser
 ├── Text PDF → PyMuPDF
 └── Scanned PDF → OCR
          │
          ▼
Text Preprocessing
          │
          ▼
SentenceTransformer Embeddings
          │
          ▼
Cosine Similarity Engine
          │
          ▼
Candidate Ranking Engine
          │
          ▼
Recruiter Dashboard
     ├── CSV Export
     └── PDF Report
```

---

This document explains the overall purpose and architecture of the project. The next section covers the project folder structure, module descriptions, AI workflow, OCR workflow, and data flow.
# Project Structure

The project follows a modular architecture where each component is responsible for a single task. This separation improves code readability, simplifies debugging, and makes future enhancements easier.

```
AI-Resume-Screening-and-Candidate-Ranking-System/
│
├── app.py
├── requirements.txt
├── README.md
├── PROJECT_BLUEPRINT.md
├── .gitignore
├── LICENSE
│
├── assets/
├── data/
│   ├── job_descriptions/
│   └── resumes/
│
├── results/
├── uploads/
├── screenshots/
│
└── utils/
    ├── __init__.py
    ├── parser.py
    ├── preprocessing.py
    ├── embedding.py
    ├── similarity.py
    ├── ranking.py
    ├── export.py
    └── pdf_report.py
```

---

# Module Description

The application is divided into independent modules, each responsible for one stage of the resume screening pipeline.

## app.py

This is the main entry point of the application. It manages the Streamlit user interface, handles file uploads, coordinates the processing pipeline, and displays the ranking dashboard and downloadable reports.

---

## parser.py

This module extracts text from uploaded resumes.

The parser first attempts to read machine-readable text using **PyMuPDF**. If no text is found, the system automatically switches to **Tesseract OCR** to process scanned or image-based PDF files.

This hybrid approach allows the application to support multiple resume formats without requiring user intervention.

---

## preprocessing.py

Raw resume text often contains unnecessary spaces, inconsistent formatting, and unwanted characters.

This module cleans and normalizes the extracted text before it is passed to the AI model. Consistent preprocessing improves the quality of semantic embeddings and similarity calculations.

---

## embedding.py

This module converts textual data into dense vector representations using the **SentenceTransformer (all-MiniLM-L6-v2)** model.

These embeddings capture the contextual meaning of the text, allowing the system to compare resumes and job descriptions based on semantic similarity rather than exact keyword matches.

---

## similarity.py

After embeddings are generated, this module calculates the similarity between the job description and each resume using **Cosine Similarity**.

The resulting similarity score represents how closely a candidate matches the job requirements.

---

## ranking.py

This module sorts candidates according to their similarity scores.

It also assigns recruiter-friendly recommendation labels such as:

- ⭐ Highly Recommended
- ✅ Recommended
- ⚠ Consider
- ❌ Not Recommended

These recommendations help recruiters interpret the ranking more easily.

---

## export.py

This module generates downloadable CSV reports containing candidate rankings and similarity scores.

The exported report can be used for documentation or further analysis.

---

## pdf_report.py

This module generates a structured PDF report summarizing the screening results.

The report includes candidate rankings and match scores, allowing recruiters to share or archive screening outcomes.

---

# AI Workflow

The AI pipeline transforms both the job description and resumes into semantic representations before comparing them.

```
Job Description
        │
        ▼
Text Preprocessing
        │
        ▼
SentenceTransformer
        │
        ▼
Embedding Vector
```

```
Resume
      │
      ▼
Parser
      │
      ▼
Text Preprocessing
      │
      ▼
SentenceTransformer
      │
      ▼
Embedding Vector
```

The embedding vectors are then compared using Cosine Similarity to generate the final ranking score.

---

# OCR Workflow

The application automatically detects whether a resume contains selectable text.

```
Resume PDF
      │
      ▼
PyMuPDF Parser
      │
      ├── Text Found
      │        │
      │        ▼
      │   Continue Processing
      │
      └── No Text Found
               │
               ▼
        Tesseract OCR
               │
               ▼
      Extract Resume Text
               │
               ▼
      Continue AI Processing
```

This hybrid workflow enables support for both digital and scanned resumes.

---

# Candidate Ranking Process

The ranking process follows these stages:

1. Upload the Job Description.
2. Upload one or more resumes.
3. Extract text from each resume.
4. Perform OCR when required.
5. Clean and preprocess the extracted text.
6. Generate semantic embeddings.
7. Calculate cosine similarity.
8. Rank candidates from highest to lowest score.
9. Display recommendations and dashboard metrics.
10. Allow CSV and PDF report downloads.

---

# Data Flow

```
Recruiter
     │
     ▼
Upload Job Description
     │
Upload Resumes
     │
     ▼
Hybrid Parser
     │
     ▼
Preprocessing
     │
     ▼
Embedding Generation
     │
     ▼
Cosine Similarity
     │
     ▼
Ranking Engine
     │
     ▼
Dashboard
     │
     ├── CSV Report
     └── PDF Report
```

---

The next section explains how to install and run the project on both Ubuntu Linux and Windows systems, followed by a complete usage guide and sample workflow.
# Installation Guide

The following steps explain how to set up and run the project on both Ubuntu Linux and Windows.

---

## Ubuntu Installation

### 1. Clone the Repository

```bash
git clone https://github.com/latent-gk12/AI-Resume-Screening-and-Candidate-Ranking-Tool.git
```

### 2. Navigate to the Project Directory

```bash
cd AI-Resume-Screening-and-Candidate-Ranking-Tool
```

### 3. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 4. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

### 5. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 6. Install OCR Dependencies

```bash
sudo apt update
sudo apt install tesseract-ocr poppler-utils
```

### 7. Launch the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

---

## Windows Installation

### 1. Clone the Repository

```powershell
git clone https://github.com/latent-gk12/AI-Resume-Screening-and-Candidate-Ranking-Tool.git
```

### 2. Navigate to the Project Directory

```powershell
cd AI-Resume-Screening-and-Candidate-Ranking-Tool
```

### 3. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 4. Activate the Environment

```powershell
.venv\Scripts\activate
```

### 5. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 6. Run the Application

```powershell
streamlit run app.py
```

---

# Project Workflow

The application follows the workflow below:

```
Recruiter
      │
      ▼
Upload Job Description
      │
Upload Candidate Resumes
      │
      ▼
Hybrid Resume Parsing
      │
      ▼
Text Preprocessing
      │
      ▼
Semantic Embedding Generation
      │
      ▼
Cosine Similarity Matching
      │
      ▼
Candidate Ranking
      │
      ▼
Dashboard Visualization
      │
      ├── CSV Export
      └── PDF Report
```

---

# How to Use the Application

After launching the application:

### Step 1

Upload the Job Description in **.txt** format.

---

### Step 2

Upload one or more candidate resumes in **PDF** format.

Both text-based and scanned resumes are supported.

---

### Step 3

Click the **Start Screening** button.

The system automatically:

- Extracts resume text.
- Performs OCR when required.
- Cleans the extracted text.
- Generates semantic embeddings.
- Calculates similarity scores.
- Ranks all candidates.

---

### Step 4

Review the ranking dashboard.

The dashboard displays:

- Total Candidates
- Best Candidate
- Match Scores
- Recommendations
- Candidate Ranking Table

---

### Step 5

Download the generated reports.

Available formats include:

- CSV Report
- PDF Candidate Ranking Report

---

# Sample Workflow

A typical recruiter interaction with the application is shown below.

1. Open the Streamlit application.

2. Upload a Job Description.

3. Upload multiple resumes.

4. Click **Start Screening**.

5. Wait for processing to complete.

6. Review the ranked candidates.

7. Download the generated reports.

The complete screening process usually takes only a few seconds depending on the number of uploaded resumes.

---

# Screenshots

The following screenshots demonstrate different stages of the application.

- Home Page
- Resume Upload Page
- OCR Processing
- Ranking Dashboard
- CSV Report
- PDF Report

Store all screenshots inside the following folder:

```
screenshots/
```

These images help readers understand the application's interface without running the project.

---

The next section covers project outputs, limitations, future improvements, contribution guidelines, license information, and acknowledgements.
# Project Outputs

After successful execution, the application generates the following outputs:

## Interactive Dashboard

The dashboard provides recruiters with an overview of the screening process, including:

- Total number of candidates screened
- Best matching candidate
- Candidate match scores
- Recommendation labels
- Candidate ranking table

This allows recruiters to quickly identify the most suitable applicants.

---

## CSV Report

The application allows recruiters to download the complete candidate ranking as a CSV file.

The exported report contains:

- Candidate Name
- Match Score
- Recommendation
- Candidate Rank

This report can be used for further analysis or record keeping.

---

## PDF Report

In addition to CSV export, the system also generates a PDF report summarizing the screening results.

The report includes:

- Candidate rankings
- Match scores
- Recommendation labels

PDF reports are useful for sharing screening results with hiring managers or maintaining recruitment documentation.

---

# Current Limitations

Although the application provides a complete AI-assisted resume screening workflow, there are a few limitations in the current version.

- Only PDF resumes are supported.
- Job descriptions must be uploaded in `.txt` format.
- Candidate names are currently identified using uploaded file names rather than automatically extracting names from resume content.
- OCR accuracy depends on the quality of scanned resumes.
- The application currently performs semantic similarity analysis but does not implement a full ATS scoring mechanism.

These limitations have been identified and planned for future development.

---

# Future Improvements

The project has been designed with scalability in mind. Future versions may include:

- Automatic candidate name extraction from resume content.
- Advanced ATS score calculation.
- Skill extraction using Named Entity Recognition (NER).
- Resume summarization using Large Language Models (LLMs).
- Recruiter authentication and role management.
- Database integration for storing screening history.
- Email notification after report generation.
- Multi-language OCR support.
- Cloud deployment using Docker and cloud platforms.
- REST API integration for third-party recruitment systems.

---

# Testing

The application has been tested using multiple resume categories to verify the complete workflow.

Testing scenarios include:

- Uploading a valid Job Description.
- Uploading multiple text-based PDF resumes.
- Uploading scanned/image-based PDF resumes.
- OCR text extraction.
- Candidate ranking generation.
- CSV report generation.
- PDF report generation.
- Invalid file handling.
- Empty input validation.

The system successfully completed all primary functional requirements for Version 1.0.

---

# Project Highlights

Some of the key achievements of this project include:

- AI-powered semantic resume matching.
- Hybrid PDF parsing with OCR fallback.
- Interactive recruiter dashboard.
- Automatic candidate ranking.
- Downloadable CSV and PDF reports.
- Modular architecture for easy maintenance.
- Clean and reusable codebase.
- Beginner-friendly project structure with industry practices.

---

# Contributing

Contributions, improvements, and suggestions are always welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new feature branch.
3. Implement your changes.
4. Commit your updates.
5. Submit a Pull Request.

Please ensure that new features maintain the modular architecture of the project.

---

# License

This project is released under the **MIT License**.

You are free to use, modify, and distribute this project for educational and personal purposes while retaining the original copyright notice.

See the `LICENSE` file for complete license information.

---

# Acknowledgements

The development of this project was made possible through the use of several open-source technologies and libraries.

Special thanks to:

- Python Community
- Streamlit
- Sentence Transformers
- Hugging Face
- Scikit-learn
- PyMuPDF
- Tesseract OCR
- ReportLab
- Pandas & NumPy
- Git & GitHub

Their contributions to the open-source ecosystem made this project possible.

---

# Author

**Garvit Sharma**

B.Tech Computer Science Engineering (Artificial Intelligence & Machine Learning)

Passionate about Artificial Intelligence, Machine Learning, Natural Language Processing, and Software Development.

GitHub Repository:

https://github.com/latent-gk12/AI-Resume-Screening-and-Candidate-Ranking-Tool

---

# Version

**Current Version:** 1.0

This release represents the first complete implementation of the AI Resume Screening & Candidate Ranking System, including hybrid PDF parsing, OCR support, semantic similarity ranking, interactive dashboard, and report generation.

---

Thank you for exploring this project.

Feedback, suggestions, and contributions are always appreciated.