import streamlit as st

from utils import ask_gemini
from prompts import ANALYSIS_PROMPT
from detector import detect_red_flags
from parser import extract_score, extract_risk
from verifier import verify_company

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------

st.set_page_config(
    page_title="AI Fake Job Posting Detector",
    page_icon="🚩",
    layout="wide"
)

# ---------------------------------------
# SIDEBAR
# ---------------------------------------

with st.sidebar:

    st.title("🚀 Features")

    st.success("✔ AI Scam Detection")
    st.success("✔ Rule-Based Analysis")
    st.success("✔ Trust Score")
    st.success("✔ Risk Meter")

    st.divider()

    st.info("Built using Gemini 2.5 Flash")

# ---------------------------------------
# TITLE
# ---------------------------------------

st.title("🚩 AI Fake Job Posting Detector")

st.caption(
    "Detect fraudulent job postings using AI and rule-based security analysis."
)

# ---------------------------------------
# JOB DETAILS
# ---------------------------------------

st.subheader("📋 Job Details")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input(
        "🏢 Company Name",
        placeholder="Google"
    )

with col2:
    job_title = st.text_input(
        "💼 Job Title",
        placeholder="Software Engineer"
    )

location = st.text_input(
    "🌍 Job Location",
    placeholder="Bangalore"
)

job_description = st.text_area(
    "📄 Job Description",
    height=250,
    placeholder="Paste the complete job posting here..."
)

# ---------------------------------------
# BUTTON
# ---------------------------------------

analyze = st.button(
    "🚀 Analyze Job Posting",
    use_container_width=True
)

# ---------------------------------------
# ANALYSIS
# ---------------------------------------

if analyze:

    if (
        not company.strip()
        or not job_title.strip()
        or not location.strip()
        or not job_description.strip()
    ):

        st.warning("Please complete all fields.")

    else:

        # Rule-Based Detection
        flags = detect_red_flags(job_description)
        company_info = verify_company(company)
        # Complete Job Information
        full_job = f"""
Company:
{company}

Job Title:
{job_title}

Location:
{location}

Description:
{job_description}
"""

        # Gemini Prompt
        prompt = ANALYSIS_PROMPT.format(
            job_description=full_job
        )

        # AI Analysis
        with st.spinner("🔍 Analyzing job posting..."):

            result = ask_gemini(prompt)

        # ---------------------------------------
        # DASHBOARD
        # ---------------------------------------

        st.divider()

        score = extract_score(result)
        risk = extract_risk(result)

        # Metrics
        metric1, metric2 = st.columns(2)

        with metric1:
            st.metric(
                label="🎯 Trust Score",
                value=f"{score}/100",
                delta=f"{score-50} vs baseline"
        )

        with metric2:
            if risk == "Low":
                st.success("🟢 Low Risk")

            elif risk == "Medium":
                st.warning("🟡 Medium Risk")

            else:
                st.error("🔴 High Risk")

        st.progress(score / 100)
        # ---------------------------------------
# COMPANY VERIFICATION
# ---------------------------------------

        st.subheader("🏢 Company Verification")

        if company_info["website_status"]:
            st.success("✅ Official website found")

            st.write(
                f"🌐 Website: {company_info['website']}"
            )

        else:
            st.error("❌ Official website not found")

        if company_info["careers"]:
            st.success("💼 Careers page available")

        else:
            st.warning("⚠ Careers page not detected")

        # ---------------------------------------
        # JOB SUMMARY
        # ---------------------------------------

        st.subheader("📋 Job Summary")

        info1, info2, info3 = st.columns(3)

        with info1:
            st.info(f"🏢 **Company**\n\n{company}")

        with info2:
            st.info(f"💼 **Role**\n\n{job_title}")

        with info3:
            st.info(f"🌍 **Location**\n\n{location}")

# ---------------------------------------
# TABS
# ---------------------------------------

        tab1, tab2 = st.tabs(["📊 Overview", "🤖 AI Analysis"])

# -------------------- TAB 1 --------------------

        with tab1:

            st.subheader("🚩 Rule-Based Detection")

            if flags:
                for flag in flags:
                    st.error(flag)
            else:
                st.success("✅ No obvious scam patterns detected.")

            st.divider()

            st.subheader("📈 Trust Meter")

            st.progress(score / 100)

# -------------------- TAB 2 --------------------

        with tab2:

            st.subheader("🤖 Detailed AI Analysis")

        with st.expander("📄 View Complete AI Report", expanded=True):
            st.markdown(result)