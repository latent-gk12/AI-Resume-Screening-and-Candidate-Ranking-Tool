# PROJECT BLUEPRINT

## AI Resume Screening & Candidate Ranking System

**Document Version:** 1.0

**Project Status:** Completed (Version 1.0)

---

# Executive Summary

This document describes the technical design, architectural decisions, development strategy, and implementation details of the AI Resume Screening & Candidate Ranking System.

The purpose of this blueprint is to provide a complete technical reference for developers who want to understand, maintain, extend, or deploy the application.

Unlike the README, which focuses on project usage, this document focuses on the internal system design and engineering decisions behind the implementation.

---

# Project Vision

The long-term vision of this project is to develop an intelligent recruitment platform capable of assisting recruiters throughout the complete hiring process.

Version 1.0 focuses on automating the initial screening stage by evaluating resumes against a job description using semantic similarity.

The architecture has been intentionally designed to support future integration of advanced recruitment features such as ATS scoring, skill extraction, recruiter authentication, interview scheduling, cloud deployment, analytics, and Large Language Models (LLMs).

---

# Design Philosophy

During development, the following principles were adopted.

### 1. Modular Design

Every major responsibility is implemented in an independent module.

This allows future improvements without affecting unrelated components.

---

### 2. Separation of Responsibilities

Each module performs only one task.

Examples include:

- Resume Parsing
- Text Preprocessing
- Embedding Generation
- Similarity Calculation
- Candidate Ranking
- Report Generation

This makes debugging and maintenance significantly easier.

---

### 3. Scalability

The architecture is intentionally designed so additional AI models, databases, authentication systems, REST APIs, or cloud services can be integrated without redesigning the complete application.

---

### 4. Maintainability

The project follows a simple folder hierarchy with reusable utility modules.

Developers can modify one module without introducing unnecessary changes throughout the application.

---

### 5. User-Centered Design

Although the backend performs AI processing, the user interface is designed for recruiters with minimal technical knowledge.

The application requires only three basic actions:

- Upload Job Description
- Upload Resumes
- Start Screening

The remaining workflow is fully automated.

---

# Business Requirements

The system has been designed to satisfy the following business requirements.

| ID | Requirement |
|----|-------------|
| BR-01 | Reduce manual resume screening effort |
| BR-02 | Improve candidate evaluation consistency |
| BR-03 | Support multiple resume uploads |
| BR-04 | Support scanned and text-based PDF resumes |
| BR-05 | Produce ranked candidate reports |
| BR-06 | Provide a simple recruiter interface |
| BR-07 | Enable future feature expansion |

---

# Functional Requirements

The current version of the application provides the following functionality.

| ID | Description |
|----|-------------|
| FR-01 | Upload Job Description |
| FR-02 | Upload Multiple Resumes |
| FR-03 | Parse PDF Files |
| FR-04 | OCR for Scanned PDFs |
| FR-05 | Text Preprocessing |
| FR-06 | Generate Semantic Embeddings |
| FR-07 | Calculate Cosine Similarity |
| FR-08 | Rank Candidates |
| FR-09 | Display Dashboard |
| FR-10 | Export CSV |
| FR-11 | Export PDF Report |

---

# Non-Functional Requirements

The system also satisfies several quality requirements.

### Performance

The application should process multiple resumes within a few seconds under normal hardware conditions.

---

### Reliability

The application should continue processing remaining resumes even if one uploaded file cannot be parsed successfully.

---

### Maintainability

Each component should remain independent to simplify future updates.

---

### Scalability

Future AI models, databases, APIs, and authentication systems should be integrated without modifying the core workflow.

---

### Usability

The complete workflow should require minimal technical knowledge from the end user.

---

# System Context

The current system operates as a standalone desktop web application.

```
Recruiter
      │
      ▼
Streamlit Interface
      │
      ▼
AI Processing Engine
      │
      ▼
Ranking Dashboard
      │
      ▼
Reports
```

Version 1.0 does not depend on cloud infrastructure or external databases.

This design keeps deployment simple while leaving room for future migration to production environments.

---

# Architecture Principles

The project follows a layered architecture consisting of four logical layers.

```
Presentation Layer

↓

Business Logic Layer

↓

AI Processing Layer

↓

Reporting Layer
```

Each layer communicates only with adjacent layers, reducing coupling between modules.

---

# Software Architecture

The application follows a layered architecture to separate user interaction, business logic, AI processing, and reporting. This structure improves maintainability and allows future enhancements without major changes to the existing codebase.

```
┌──────────────────────────────┐
│     Presentation Layer       │
│      (Streamlit UI)          │
└──────────────┬───────────────┘
               │
┌──────────────▼───────────────┐
│    Application Logic Layer   │
│      (app.py Controller)     │
└──────────────┬───────────────┘
               │
┌──────────────▼───────────────┐
│      AI Processing Layer     │
│ Parser → NLP → Ranking       │
└──────────────┬───────────────┘
               │
┌──────────────▼───────────────┐
│      Reporting Layer         │
│ CSV Export & PDF Reports     │
└──────────────────────────────┘
```

Each layer has a well-defined responsibility and communicates only with adjacent layers.

---

# Request Lifecycle

The following sequence describes how the application processes a screening request from start to finish.

```
Recruiter
      │
      ▼
Upload Job Description
      │
Upload Resume Files
      │
      ▼
Input Validation
      │
      ▼
Resume Parsing
      │
      ▼
OCR (if required)
      │
      ▼
Text Preprocessing
      │
      ▼
Embedding Generation
      │
      ▼
Similarity Calculation
      │
      ▼
Candidate Ranking
      │
      ▼
Dashboard Rendering
      │
      ▼
CSV / PDF Export
```

Each stage completes before passing data to the next stage, creating a predictable and maintainable processing pipeline.

---

# Internal Module Interaction

The application modules communicate in the following order.

```
app.py
   │
   ├── parser.py
   │
   ├── preprocessing.py
   │
   ├── embedding.py
   │
   ├── similarity.py
   │
   ├── ranking.py
   │
   ├── export.py
   │
   └── pdf_report.py
```

The controller (`app.py`) coordinates the workflow, while each utility module performs a single responsibility.

---

# Folder Responsibilities

## data/

Stores all project datasets.

Contents include:

- Job Descriptions
- Sample Resumes

This folder can later be replaced with database storage without affecting the AI pipeline.

---

## uploads/

Stores files uploaded during execution if persistence is required.

In the current implementation, uploaded files are processed directly through Streamlit, making this directory optional for Version 1.0.

---

## results/

Stores generated output files such as:

- Candidate Ranking CSV
- PDF Screening Reports

Keeping generated reports separate from application logic improves project organization.

---

## assets/

Reserved for project assets including:

- Logos
- Icons
- Documentation images
- Static resources

Although lightly used in Version 1.0, this directory supports future UI improvements.

---

## screenshots/

Contains screenshots referenced in the README.

These images provide visual documentation of the application and should not contain sensitive or personal information.

---

## utils/

This directory contains reusable modules that implement the application's core logic.

Each file is responsible for one stage of the processing pipeline, allowing individual components to be tested and maintained independently.

---

# Dependency Relationships

The project intentionally avoids unnecessary coupling between modules.

```
Parser
   │
   ▼
Preprocessing
   │
   ▼
Embedding
   │
   ▼
Similarity
   │
   ▼
Ranking
   │
   ▼
Reporting
```

Each module depends only on the output of the previous stage, reducing complexity and improving maintainability.

---

# Error Handling Strategy

The application includes basic validation and exception handling to improve reliability.

Current validation includes:

- Missing Job Description
- Missing Resume Upload
- Invalid File Type
- Empty PDF Detection
- OCR Fallback for Non-Readable PDFs
- Exception Handling during Parsing

Rather than terminating the entire workflow, the application is designed to continue processing remaining valid inputs whenever possible.

---

# Design Decisions

Several implementation decisions were made to balance functionality, simplicity, and extensibility.

### Why Streamlit?

Streamlit enables rapid development of interactive web applications using pure Python, making it suitable for AI-focused projects without requiring frontend frameworks.

---

### Why Sentence Transformers?

Semantic embeddings provide contextual understanding of text, allowing resumes to be matched based on meaning rather than exact keywords.

This improves candidate ranking compared to traditional keyword matching.

---

### Why Cosine Similarity?

Cosine Similarity is computationally efficient and widely used for comparing high-dimensional embedding vectors.

It provides an effective measure of semantic closeness between resumes and job descriptions.

---

### Why Hybrid PDF Parsing?

Real-world recruitment involves both digitally generated and scanned resumes.

Using only a PDF parser would fail on scanned documents.

Using only OCR would unnecessarily slow processing for text-based PDFs.

The hybrid approach combines the strengths of both methods by selecting the appropriate extraction technique automatically.

---

# Scalability Considerations

Although Version 1.0 is designed as a local application, the architecture supports future expansion.

Potential extensions include:

- REST API integration
- Database-backed storage
- Authentication and user roles
- Background task processing
- Containerized deployment
- Cloud hosting
- AI model replacement
- Enterprise ATS integration

Because the project follows a modular design, these additions can be introduced with minimal changes to the existing workflow.

---
# AI Processing Pipeline

The AI processing pipeline is the core component of the application. It transforms unstructured resume documents into structured numerical representations that can be compared against a job description.

The pipeline consists of five sequential stages:

```
Resume
   │
   ▼
Text Extraction
   │
   ▼
Text Preprocessing
   │
   ▼
Embedding Generation
   │
   ▼
Similarity Calculation
   │
   ▼
Candidate Ranking
```

Each stage produces the input required by the following stage, creating a consistent and reusable workflow.

---

# Resume Parsing Strategy

The application adopts a **Hybrid Resume Parsing Strategy** to maximize compatibility with real-world resumes.

Instead of relying on a single extraction technique, the parser determines the most suitable approach based on the uploaded PDF.

```
PDF Resume
      │
      ▼
PyMuPDF Extraction
      │
      ├───────────────┐
      │               │
Text Found?         No Text
      │               │
      ▼               ▼
 Continue      OCR Processing
                     │
                     ▼
             Extract Resume Text
```

This approach provides two major advantages:

- Faster processing for digital PDFs.
- Support for scanned or image-based resumes without changing the user workflow.

---

# OCR Pipeline

For scanned resumes, the application uses **Tesseract OCR**.

The OCR workflow consists of the following steps:

```
Scanned Resume
        │
        ▼
Convert PDF Pages to Images
        │
        ▼
Image Enhancement
        │
        ▼
Tesseract OCR
        │
        ▼
Extract Text
        │
        ▼
Preprocessing
```

### OCR Components

| Component | Purpose |
|-----------|---------|
| pdf2image | Converts PDF pages into images |
| Pillow | Loads and processes images |
| Tesseract OCR | Extracts text from images |

This design allows the application to process resumes that cannot be parsed directly.

---

# Text Preprocessing

The extracted resume text is normalized before AI processing.

Current preprocessing includes:

- Converting text to lowercase
- Removing extra whitespace
- Removing unnecessary special characters
- Basic text normalization

The objective is to produce clean and consistent input for the embedding model.

Future versions may include:

- Stop-word removal
- Lemmatization
- Named Entity Recognition (NER)
- Skill extraction

---

# Embedding Generation

The application uses the **SentenceTransformer** model:

```
all-MiniLM-L6-v2
```

This model converts textual content into fixed-length embedding vectors.

Instead of matching exact keywords, embeddings represent the contextual meaning of sentences.

Example:

```
Resume

↓

SentenceTransformer

↓

384-dimensional Vector
```

Both the job description and every resume are converted into embedding vectors before similarity comparison.

---

# Similarity Calculation

The similarity between the Job Description and each Resume is calculated using **Cosine Similarity**.

```
Job Embedding
       │
       ▼
Cosine Similarity
       ▲
       │
Resume Embedding
```

The resulting value is converted into a percentage and used as the candidate's **Match Score**.

A higher similarity score indicates stronger alignment between the resume and the job description.

---

# Candidate Ranking Logic

Once similarity scores have been calculated, the system performs the following operations:

1. Store all candidate scores.
2. Sort candidates in descending order.
3. Assign ranking positions.
4. Generate recommendation labels.
5. Display results in the dashboard.
6. Enable CSV and PDF export.

This ensures recruiters receive an organized and interpretable summary of all applicants.

---

# Recommendation Strategy

Recommendation labels are generated from similarity score ranges.

| Match Score | Recommendation |
|-------------|----------------|
| ≥ 80% | ⭐ Highly Recommended |
| 65% – 79% | ✅ Recommended |
| 50% – 64% | ⚠ Consider |
| < 50% | ❌ Not Recommended |

These thresholds are configurable and can be adjusted according to organizational hiring policies.

---

# Performance Considerations

Version 1.0 has been optimized for simplicity and responsiveness.

Current optimizations include:

- Lightweight embedding model.
- Hybrid parsing to avoid unnecessary OCR execution.
- Modular processing pipeline.
- In-memory data handling for faster execution.
- Sequential workflow to simplify debugging.

Future optimization opportunities include:

- Parallel resume processing.
- Batch embedding generation.
- GPU acceleration.
- Embedding caching.
- Asynchronous task execution.

---

# Security Considerations

Although the application is designed as a local desktop tool, several basic security practices have been considered.

Current measures include:

- Local processing of uploaded resumes.
- No external API calls during screening.
- No permanent storage of uploaded documents by default.
- No collection of personal user credentials.

Future enterprise versions may include:

- User authentication.
- Role-based access control.
- Resume encryption.
- Audit logging.
- Secure cloud storage.
- Database backups.

---

# Engineering Decisions

The following design choices were made during development.

| Decision | Reason |
|----------|--------|
| Streamlit | Rapid AI application development |
| Modular Architecture | Easier maintenance and scalability |
| SentenceTransformer | Better semantic understanding than keyword matching |
| Cosine Similarity | Efficient vector comparison |
| PyMuPDF | Fast extraction from text PDFs |
| OCR Fallback | Support scanned resumes |
| ReportLab | Lightweight PDF report generation |
| CSV Export | Easy integration with spreadsheet tools |

---

# Testing Strategy

To ensure reliability, the application was tested at both the module level and the complete workflow level.

## Module Testing

Each utility module was tested independently before integrating it into the main application.

| Module | Testing Objective | Status |
|----------|------------------|--------|
| parser.py | Extract text from text-based and scanned PDFs | ✅ Passed |
| preprocessing.py | Clean and normalize extracted text | ✅ Passed |
| embedding.py | Generate semantic embeddings | ✅ Passed |
| similarity.py | Calculate cosine similarity | ✅ Passed |
| ranking.py | Rank candidates and assign recommendations | ✅ Passed |
| export.py | Generate CSV reports | ✅ Passed |
| pdf_report.py | Generate PDF reports | ✅ Passed |

---

## Integration Testing

The complete application workflow was validated using multiple job descriptions and resume datasets.

The following scenarios were tested:

- Upload valid job description
- Upload multiple resumes
- Upload scanned resumes
- OCR fallback execution
- Candidate ranking generation
- CSV report generation
- PDF report generation
- Dashboard rendering
- Empty input validation
- Invalid file handling

The system successfully completed all functional requirements for Version 1.0.

---

# Deployment Strategy

The current version is designed as a local desktop web application.

Deployment process:

```
Developer
      │
      ▼
GitHub Repository
      │
      ▼
Clone Project
      │
      ▼
Install Dependencies
      │
      ▼
Run Streamlit
      │
      ▼
Local Web Application
```

This deployment approach was selected because it:

- Requires minimal configuration.
- Is suitable for academic and internship demonstrations.
- Supports rapid testing and development.

Future versions may be deployed using Docker and cloud platforms.

---

# Risks and Limitations

Every software system has limitations. Identifying them helps define future improvements.

Current limitations include:

- Supports only PDF resumes.
- Job descriptions are accepted only in text format.
- Candidate names are identified from uploaded file names.
- OCR accuracy depends on scan quality.
- Resume screening focuses on semantic similarity rather than a complete ATS evaluation.
- No persistent database storage.
- No recruiter authentication or user management.

These limitations were accepted to maintain a manageable scope for Version 1.0 while keeping the architecture extensible.

---

# Future Roadmap

The project roadmap is divided into multiple versions.

## Version 1.1

- Automatic candidate name extraction.
- Improved OCR preprocessing.
- Enhanced recommendation logic.
- Better PDF report formatting.

---

## Version 1.2

- Skill extraction using Named Entity Recognition (NER).
- ATS compatibility score.
- Resume keyword analytics.
- Recruiter dashboard enhancements.

---

## Version 2.0

- User authentication and authorization.
- Database integration.
- Screening history management.
- Recruiter profile management.
- Resume repository.

---

## Version 3.0

- REST API implementation.
- Docker containerization.
- Cloud deployment.
- Enterprise ATS integration.
- Resume recommendation engine.
- Interview scheduling.

---

## Version 4.0

- Large Language Model (LLM) integration.
- AI-generated resume summaries.
- Interview question generation.
- Candidate feedback generation.
- Multi-language resume analysis.
- AI-powered recruitment assistant.

---

# Deliverables

The final Version 1.0 release includes:

- Streamlit Web Application
- Hybrid Resume Parser
- OCR Integration
- NLP-based Resume Screening
- Semantic Similarity Matching
- Candidate Ranking Engine
- Dashboard Metrics
- Progress Indicator
- CSV Export
- PDF Report Generation
- Technical Documentation
- GitHub Repository

---

# Version History

| Version | Description |
|----------|-------------|
| 0.1 | Initial project planning |
| 0.5 | Resume parsing and preprocessing |
| 0.7 | SentenceTransformer integration |
| 0.8 | Candidate ranking implementation |
| 0.9 | OCR support and report generation |
| 1.0 | Stable release with complete documentation |

---

# Lessons Learned

During the development of this project, several important engineering concepts were applied:

- Modular software architecture.
- Practical Natural Language Processing.
- Semantic similarity using transformer models.
- OCR integration for document processing.
- Streamlit application development.
- Report generation using Python.
- Git and GitHub version control.
- Documentation and project organization.

These concepts provide a strong foundation for developing larger AI-powered software systems.

---

# Conclusion

The AI Resume Screening & Candidate Ranking System demonstrates how Artificial Intelligence can improve the efficiency of recruitment workflows through semantic resume analysis and automated candidate ranking.

Version 1.0 successfully integrates hybrid PDF parsing, OCR support, NLP-based semantic matching, interactive visualization, and report generation into a single modular application. The architecture has been intentionally designed to support future enhancements without requiring major structural changes.

This project serves as a practical demonstration of AI, NLP, software engineering, and documentation practices, making it suitable for academic evaluation, internship submissions, portfolio presentation, and future extension into an enterprise-grade recruitment platform.

---

# Document Information

**Document Name:** TECHNICAL_BLUEPRINT.md

**Project Name:** AI Resume Screening & Candidate Ranking System

**Version:** 1.0

**Status:** Final

**Prepared By:** Garvit Sharma

**Technology Stack:** Python, Streamlit, Sentence Transformers, PyMuPDF, Tesseract OCR, Scikit-learn, Pandas, NumPy, ReportLab

---

**End of Technical Blueprint** 