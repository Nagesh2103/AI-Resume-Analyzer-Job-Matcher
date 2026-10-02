# AI Resume Analyzer & Job Matcher

An AI-powered resume analysis and job matching application built with **Python, Streamlit, LangChain, and Google Gemini**.

The application allows users to upload their resume in **PDF or DOCX format**, provide a job description, and receive an AI-powered analysis of their resume, job requirements, skill compatibility, and recommendations for improving their resume for the target role.

---

## 🚀 Features

* 📄 Upload resumes in **PDF** or **DOCX** format
* 🤖 AI-powered resume analysis using **Google Gemini**
* 💼 Analyze and extract requirements from job descriptions
* 🔍 Compare resume skills with job requirements
* 📊 Generate a **job match score**
* ✅ Identify matched skills
* ⚠️ Identify partially matched skills
* ❌ Identify missing skills
* 📋 Analyze candidate experience, education, projects, and certifications
* 💡 Generate AI-powered resume improvement recommendations
* 🔑 Identify missing keywords and skills to highlight
* 📑 Provide ATS-oriented resume recommendations
* 🖥️ Interactive web interface built with Streamlit

---

## 🛠️ Technologies Used

### Programming Language

* Python

### AI / LLM

* Google Gemini
* LangChain
* `langchain-google-genai`

### Application Framework

* Streamlit

### Resume Processing

* PyMuPDF (`fitz`) – PDF text extraction
* `python-docx` – DOCX text extraction

### Environment & Configuration

* `python-dotenv`

---

## 🏗️ Project Architecture

```text
Resume_Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── data/
│
├── output/
│
└── utils/
    ├── llm.py
    ├── matcher.py
    ├── prompts.py
    └── resume_parser.py
```

### File Description

| File / Directory         | Description                                                               |
| ------------------------ | ------------------------------------------------------------------------- |
| `app.py`                 | Main Streamlit application and user interface                             |
| `requirements.txt`       | Python dependencies required by the project                               |
| `utils/llm.py`           | Handles Gemini LLM initialization and AI analysis                         |
| `utils/resume_parser.py` | Extracts text from PDF and DOCX resumes                                   |
| `utils/matcher.py`       | Calculates the match level from the match score                           |
| `utils/prompts.py`       | Contains prompts used for resume, job, matching, and improvement analysis |
| `data/`                  | Directory for project data                                                |
| `output/`                | Directory for generated/output files                                      |

---

## 🔄 How the Application Works

The application follows the workflow below:

```text
Resume Upload
     │
     ▼
PDF / DOCX Text Extraction
     │
     ▼
AI Resume Analysis
     │
     ├── Candidate Information
     ├── Skills
     ├── Programming Languages
     ├── Tools & Technologies
     ├── Education
     ├── Experience
     ├── Projects
     └── Certifications
     
Job Description
     │
     ▼
AI Job Description Analysis
     │
     ├── Required Skills
     ├── Preferred Skills
     ├── Programming Languages
     ├── Tools & Technologies
     ├── Experience
     ├── Responsibilities
     └── Education
     
     ▼
Resume ↔ Job Matching
     │
     ├── Match Score
     ├── Matched Skills
     ├── Partially Matched Skills
     ├── Missing Skills
     ├── Experience Match
     ├── Strengths
     └── Weaknesses
     
     ▼
AI Resume Recommendations
     │
     ├── Missing Keywords
     ├── Skills to Highlight
     ├── Section Improvements
     ├── Project Improvements
     └── ATS Recommendations
```

---

## 📊 Application Output

After analysis, the application provides four main sections.

### 1. Resume Analysis

The application extracts and analyzes:

* Name
* Email
* Phone
* Professional summary
* Skills
* Programming languages
* Tools and technologies
* Education
* Experience
* Projects
* Certifications

### 2. Job Analysis

The job description is analyzed to identify:

* Required skills
* Preferred skills
* Programming languages
* Tools and technologies
* Required experience
* Responsibilities
* Education requirements

### 3. Skill Matching

The application compares the analyzed resume with the job requirements and provides:

* Match score
* Match level
* Matched skills
* Partially matched skills
* Missing skills
* Experience match
* Strengths
* Weaknesses

The current match-level classification is:

| Match Score | Match Level     |
| ----------: | --------------- |
|      80–100 | Excellent Match |
|       60–79 | Good Match      |
|       40–59 | Moderate Match  |
|        0–39 | Low Match       |

### 4. AI Recommendations

The application generates recommendations including:

* Missing keywords
* Skills to highlight
* Resume section improvements
* Project improvements
* ATS recommendations

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Resume_Analyzer.git
```

Navigate into the project:

```bash
cd Resume_Analyzer
```

---

### 2. Create a virtual environment

For Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

The application uses environment variables for API credentials.

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

The application uses Google Gemini through `langchain-google-genai`.

### ⚠️ Important

**Never commit your `.env` file to GitHub.**

Add the following to `.gitignore`:

```gitignore
.env
.env.*
!.env.example

__pycache__/
*.pyc
venv/
.venv/
.vscode/
.idea/
```

For other developers, create an example environment file:

### `.env.example`

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Do not put real API keys in `.env.example`.

---

## ▶️ Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

You can then:

1. Upload your resume.
2. Paste the target job description.
3. Click **Analyze Resume**.
4. Review the resume analysis.
5. Review the job requirements.
6. Check the skill matching results.
7. Review AI-generated resume improvement recommendations.

---

## 📦 Dependencies

The project uses the following main Python packages:

```text
streamlit
langchain
langchain-google-genai
pymupdf
python-docx
python-dotenv
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🧠 AI Prompt Architecture

The application uses separate prompts for different analysis tasks.

### Resume Analysis

Extracts structured information from the uploaded resume.

### Job Description Analysis

Extracts important requirements and responsibilities from the job description.

### Resume-Job Matching

Compares the resume analysis with the job analysis and generates a match score and skill comparison.

### Resume Improvement

Generates recommendations based on missing keywords, skills, resume sections, projects, and ATS considerations.

The AI responses are requested in JSON format so that the application can process the results programmatically.

---

## 📁 Supported Resume Formats

Currently supported:

* PDF (`.pdf`)
* Microsoft Word (`.docx`)

Unsupported file formats will generate an error requesting a PDF or DOCX file.

---

## 🔒 Security

API credentials should always be stored locally in environment variables.

Do **not** commit:

```text
.env
```

to GitHub.

If an API key is accidentally pushed to a public repository:

1. Revoke the exposed key immediately.
2. Generate a new API key.
3. Replace the key in your local `.env`.
4. Remove the secret from the repository history if necessary.

---

## 🎯 Use Cases

This project can be used to:

* Analyze a resume against a specific job description
* Identify missing technical skills
* Find important keywords from job descriptions
* Understand resume-job compatibility
* Improve resume content for specific roles
* Identify skills that should be highlighted
* Generate ATS-oriented recommendations

---

## 🔮 Future Improvements

Possible future enhancements include:

* Resume scoring based on multiple ATS criteria
* Support for additional resume formats
* Resume section-wise scoring
* More advanced semantic skill matching
* Job recommendations based on resume skills
* Resume optimization suggestions with before/after examples
* Downloadable analysis reports
* Resume history and comparison
* Authentication and user accounts
* Deployment using Streamlit Cloud or another cloud platform

---

## 👨‍💻 Author

**M S Nagesh**

Information Science Graduate | Python | Data Science | AI/ML | Generative AI

---

## ⭐ Project Purpose

This project was developed as a practical application of **Generative AI, LLM integration, document processing, prompt engineering, and Python application development**.

It demonstrates how an LLM can be integrated into an end-to-end application to analyze unstructured resume and job-description data and transform it into structured, actionable insights.
