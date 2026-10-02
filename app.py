import streamlit as st
from utils.resume_parser import extract_text

from utils.llm import (
    analyze_resume,
    analyze_job,
    match_resume_with_job,
    generate_improvements)

from utils.matcher import prepare_matching_result

st.set_page_config(
    page_title="AI Resume Analyser",
    page_icon="📄",
    layout="wide")

st.title("AI Resume Analyzer & Job Matcher")

st.write(
    "Upload your reume and enter a job description "
    "to analyze your profile and calculate your job match. ")
st.subheader("1. Upload Your Resume")

resume_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"])

st.subheader("2. Enter Job Description")

job_text = st.text_area(
    "Paste or type the Job Description here",
    height=300,
    placeholder=(
        "Paste the complete job description here...\n\n"
        "Example:\n"
        "We are looking for a Machine Learning Engineer "
        "with experience in Python, Machine Learning, "
        "Generative AI, LangChain and SQL,"))

analyze_button = st.button(
    "Analyze Resume", type="primary")

if analyze_button:
    if resume_file is None:
        st.warning("Please upload your resume. ")
        st.stop()

    if not job_text.strip():
        st.warning("Please enter the job description.")
        st.stop()

    try:
        with st.spinner("Reading your resume..."):
            resume_text = extract_text(resume_file)
        if not resume_text.strip():
            st.error("Could not extract text from the resume.")
            st.stop()
        job_text = job_text.strip()

        with st.spinner("Analyzing your resume with AI..."):
            resume_analysis = analyze_resume(resume_text)

        with st.spinner("Analyzing the job description..."):
            job_analysis = analyze_job(job_text)

        with st.spinner("Comparing your resume with the job..."):
            matching_result = match_resume_with_job(resume_analysis,job_analysis)

            matching_result = prepare_matching_result(matching_result)

        with st.spinner("Generating AI recommendations..."):
            improvements = generate_improvements(
                resume_analysis,job_analysis)

        st.session_state["resume_analysis"] = (resume_analysis)
        st.session_state["job_analysis"] = (job_analysis)
        st.session_state["matching_result"] = (matching_result)
        st.session_state["improvements"] = (improvements)
        st.success("Resume analysis completed successfully!")

    except Exception as e:
        st.error(f"Something went wrong: {str(e)}")

if "resume_analysis" in st.session_state:

    resume_analysis = st.session_state["resume_analysis"]
    job_analysis = st.session_state["job_analysis"]
    matching_result = st.session_state["matching_result"]
    improvements = st.session_state["improvements"]

    st.divider()
    st.header("Job Match")
    score = matching_result.get( "match_score",0)
    level = matching_result.get("match_level","Not Available")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Match SCore", f"{score}%")
    with col2:
        st.metric("Match Level",level)

    st.progress(min(max(score,0),100) / 100)
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Resume Analysis",
            "Job Analysis",
            "Skill Matching",
            "AI Recommendation"])
    with tab1:
        st.subheader("Candidate Information")
        st.write(
            "**Name:**",
            resume_analysis.get("name","Not available"))
        st.write(
            "**Email:**",
            resume_analysis.get("email","Not available"))
        st.write(
            "**Phone:**",
            resume_analysis.get("phone","Not available"))

        st.subheader("Professional Summary")
        st.write(resume_analysis.get("summary","Not available"))

        st.subheader("Skills")
        skills = resume_analysis.get("skills",[])
        if skills:
            st.write(", ".join(skills))
        else:
            st.write("No skills detected.")


        st.subheader("Programming Languages")
        languages = resume_analysis.get("programming_languages",[])
        if languages:
            st.write(", ".join(languages))
        else:
            st.write("No programming languages detected.")


        st.subheader("Tools & Technologies")
        tools = resume_analysis.get("tools",[])
        if tools:
            st.write(", ".join(tools))
        else:
            st.write("No tools detected.")


        st.subheader("Education")
        education = resume_analysis.get("education",[])
        for item in education:
            st.write(f"⭐ {item}")

        st.subheader("Experience")
        experience = resume_analysis.get("experience",[])
        for item in experience:
            st.write(f"⭐ {item}")

        st.subheader("Projects")
        projects = resume_analysis.get("projects",[])
        for project in projects:
            st.write(f"⭐ {project}")

        st.subheader("Certifications")
        certifications = resume_analysis.get("certifications",[])
        for certification in certifications:
            st.write(f"⭐ {certification}")

    with tab2:
        st.subheader("Required Skills")
        required_skills = job_analysis.get("required_skills",[])
        for skill in required_skills:
            st.write(f"⭐ {skill}")

        st.subheader("Preferred SKills")
        preferred_skills = job_analysis.get("preferred_skills",[])
        for skill in preferred_skills:
            st.write(f"⭐ {skill}")

        st.subheader("Programming Languages")
        languages = job_analysis.get("Programming_Languages",[])
        if languages:
            st.write(", ".join(languages))

        st.subheader("Tools & Technologies")
        tools = job_analysis.get("tools",[])
        if tools:
            st.write(", ".join(tools))

        st.subheader("Required Experience")
        st.write(job_analysis.get("experience","Not available"))

        st.subheader("Responsibilities")
        responsibilities = job_analysis.get("responsibilities",[])
        for responsibility in responsibilities:
            st.write(f"⭐ {responsibility}")

        st.subheader("Education")
        st.write(job_analysis.get("education","Not available"))

    with tab3:
        st.subheader("Matched Skills")
        matched_skills = matching_result.get("matched_skills",[])
        if matched_skills:
            for skill in matched_skills:
                st.success(skill)
        else:
            st.write("No matching skills found.")

        st.subheader("Partially Matched Skills")
        partial_skills = matching_result.get("partially_matched_skills",[])
        if partial_skills:
            for skill in partial_skills:
                st.warning(skill)
        else:
            st.write("No partially matched skills.")


        st.subheader("Missing Skills")
        missing_skills = matching_result.get("missing_skills",[])
        if missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.write("No major missing skills.")

        st.subheader("Experience Match")

        st.write(matching_result.get("experience_match","Not available"))

        st.subheader("Strengths")
        strengths = matching_result.get("strengths",[])
        for item in strengths:
            st.write(f"⭐ {item}")

        st.subheader("Weaknesses")
        weaknesses = matching_result.get("weaknesses",[])
        for item in weaknesses:
            st.write(f"⭐ {item}")

    with tab4:
        st.subheader("Missing Keywords")
        missing_keywords = improvements.get("missing_keywords",[])
        for item in missing_keywords:
            st.write(f"⭐ {item}")

        st.subheader("Skills to Highlight")
        skills_to_highlight = improvements.get("skills_to_highlight",[])
        for item in skills_to_highlight:
            st.write(f"⭐ {item}")

        st.subheader("Resume Improvements")
        section_improvements = improvements.get("section_improvements",[])
        for item in section_improvements:
            st.write(f"⭐ {item}")

        st.subheader("Project Improvements")
        project_improvements = improvements.get("project_improvements",[])
        for item in project_improvements:
            st.write(f"⭐ {item}")

        st.subheader("ATS Recommendations")
        ats_recommendations = improvements.get("ats_recommendations",[])
        for item in ats_recommendations:
            st.write(f"⭐ {item}")