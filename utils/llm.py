import os
import json

from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

from utils.prompts import (
    RESUME_ANALYSIS_PROMPT,
    JOB_ANALYSUS_PROMPT,
    MATCHING_PROMPT,
    IMPROVEMENT_PROMPT)

def get_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0)
    return llm


def clean_json_response(response):
    content = response.content
    if isinstance(content, list):
        content = "".join(
            item.get("text", "")
            if isinstance(item, dict)
            else str(item)
            for item in content)
    content = content.strip()

    # Remove markdown code fences if Gemini returns them 
    if content.startswith("```json"):
        content = content[7:]
    elif content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    content = content.strip()
    return json.loads(content)

def analyze_resume(resume_text):
    llm = get_llm()
    prompt = RESUME_ANALYSIS_PROMPT.format(resume_text=resume_text)
    response = llm.invoke(prompt)
    return clean_json_response(response)

def analyze_job(job_text):
    llm = get_llm()
    prompt = JOB_ANALYSUS_PROMPT.format(job_text=job_text)
    response = llm.invoke(prompt)
    return clean_json_response(response)


def match_resume_with_job(resume_analysis,job_analysis):
    llm = get_llm()
    prompt = MATCHING_PROMPT.format(
        resume_analysis=json.dumps(
            resume_analysis,indent=2),
        job_analysis=json.dumps(
            resume_analysis,indent=2))
    response = llm.invoke(prompt)
    return clean_json_response(response)

def generate_improvements(resume_analysis,job_analysis):
    llm = get_llm()
    prompt = IMPROVEMENT_PROMPT.format(
        resume_analysis=json.dumps(
            resume_analysis,indent=2),
        job_analysis=json.dumps(
            job_analysis,indent=2))

    response = llm.invoke(prompt)
    return clean_json_response(response)



