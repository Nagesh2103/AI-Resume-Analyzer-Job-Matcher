RESUME_ANALYSIS_PROMPT = '''
You are an expert resume analyzer.
Analyze the following resume and extract the important information.
Resume :
{resume_text}
Return only valid JSON in the following format :
{{
    "name" : "",
    "email" : "",
    "phone" : "",
    "summary" : "",
    "skills" : [],
    "programming_languages" : [],
    "tools" : [],
    "education" : [],
    "experience" : [],
    "projects" : [],
    "certifications" : []
    
}}
'''


JOB_ANALYSUS_PROMPT = """
You are an expert job discription analyzer.
Analyzer the following job discription.
Job Description:
{job_text}
Extract :
1. Required skills
2. Preferred skills
3. Programming languages
4. Tools and technologies
5. Required experience
6. Responsibilities
7. Education requirements
Return ONLY valid JSON in this fomat:
{{
    "required_skills" : [],
    "preferred_skills" : [],
    "programming_languages" : [],
    "tools" : [].
    "experience" : "",
    "responsibilities : [],
    "education" :""
}}
"""


MATCHING_PROMPT="""
You are an expert technical recruiter.
Compare the resume with the job description.
RESUME ANALYSIS:
{resume_analysis}
JOB ANALYSIS:
{job_analysis}
Analyze how well the candidate matches the job.
Return ONLY valid JSON in this format:
{{
    "match_score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "partially_matched_skills":[],
    "experience_match":"",
    "strengths":[],
    "weaknesses":[],
    "recommendations":[]
}}
The match_score must be between 0 and 100.
"""


IMPROVEMENT_PROMPT = """
You are an expert ATS resume consultant.
Based on the resume analysis and job analysis below, provide
specific suggestions to improve the resume for this job.
Resume:
{resume_analysis}
Job:
{job_analysis}
Provide:
1. Missing keywords
2. Skills that should be highlighted
3. Resume sections that need improvement
4. Project improvements
5. ATS recommendations
Return ONLY valid JSON:
{{
    "missing_keywords": [],
    "skills_to_highlight": [],
    "section_improvements": [],
    "project_improvements": [],
    "ats_recommendations": []
}}"""