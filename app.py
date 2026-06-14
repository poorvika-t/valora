import streamlit as st
from hindsight_client import Hindsight
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(
    page_title="Valora",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>

/* Main App */
.main {
    padding-top: 1rem;
}
h1 {
    font-size: 3.5rem !important;
}

h2 {
    font-size: 2.2rem !important;
}

h3 {
    font-size: 1.6rem !important;
}

.stMarkdown {
    font-size: 20px !important;
}
/* Bigger title */
h1 {
    font-size: 3rem !important;
    font-weight: 700 !important;
}

/* Bigger section headers */
h2 {
    font-size: 2rem !important;
    font-weight: 600 !important;
}

/* Bigger text */
p, label, div {
    font-size: 18px !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #1e293b;
}
            
[data-testid="stSidebar"] * {
    color: white !important;
}

[data-testid="stSidebar"] * {
    font-size: 17px !important;
}

/* Buttons */
.stButton button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}

/* Inputs */
.stTextInput input {
    font-size: 18px !important;
}

.stTextArea textarea {
    font-size: 18px !important;
}

/* Metric cards */
[data-testid="metric-container"] {
    background-color: #1f2937;
    border-radius: 12px;
    padding: 20px;
    border: 1px solid #374151;
}

/* Success messages */
.stSuccess {
    border-radius: 10px;
}

/* Info boxes */
.stInfo {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)
debug_mode = st.checkbox("Show Memory Retrieval")
# Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Hindsight Client
hindsight = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

st.sidebar.title("Valora")

st.sidebar.markdown("""
### AI Fundraising Intelligence

Transform startup history into investor insights.

---

### Platform Modules

📊 Investor Insights

🎯 Startup Pitch Predictor

🧠 Investment Outcome Logger

🤝 Investment Match Maker

📝 Similar Startup Finder

---

Built using:

• Groq LLM

• Hindsight Memory

• Streamlit
""")
page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Ask Valora",
        "Investor Insights",
        "Startup Pitch Predictor",
        "Investment Outcome Logger",
        "Similar Startup Finder",
        "Investor Matchmaker"
    ]
)
if page == "Dashboard":

    st.title("🚀 Valora")

    st.markdown("""
                <h1 style='font-size:48px;'>
                AI-Powered Fundraising Intelligence
                </h1>
                <p style='font-size:24px; font-weight:600;'>
                Turn startup history into investor intelligence.
                </p>
                <p style='font-size:20px;'>
                Valora learns from past investor decisions, startup outcomes,
                and fundraising patterns to help founders raise capital smarter.
                </p>
                """, unsafe_allow_html=True)
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
                    <div style="
                    background:#1e293b;
                    padding:25px;
                    border-radius:15px;
                    text-align:center;
                    color:white;">
                    <h2 style="color:white;">📚</h2>
                    <h1 style="color:white;">70+</h1>
                    <p style="color:white;">Investor Memories</p>
                    </div>
                    """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
                    <div style="
                    background:#1e293b;
                    padding:25px;
                    border-radius:15px;
                    text-align:center;
                    color:white;">
                    <h2 style="color:white;">💼</h2>
                    <h1 style="color:white;">10+</h1>
                    <p style="color:white;">Investors Tracked</p>
                    </div>
                    """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
                    <div style="
                    background:#1e293b;
                    padding:25px;
                    border-radius:15px;
                    text-align:center;
                    color:white;">
                    <h2 style="color:white;">🚀</h2>
                    <h1 style="color:white;">70+</h1>
                    <p style="color:white;">Startup Cases</p>
                    </div>
                    """, unsafe_allow_html=True)
        st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
                    ## What Valora Can Do

                    ✅ Analyze investor behavior

                    ✅ Predict fundraising readiness

                    ✅ Match startups with investors

                    ✅ Learn from historical startup outcomes

                    ✅ Build long-term institutional memory
                    """)

    with col2:
        st.markdown("""
                    ## Powered By

                    🧠 Hindsight Memory

                    ⚡ Groq LLM

                    📊 Investor Intelligence Engine

                    🚀 Startup Pattern Analysis

                    💡 Fundraising Recommendation System
                    """)
    st.divider()
    st.success(
            "Ready to explore? Use the navigation menu on the left."
        )
# -----------------------------
# NORMAL CHAT SECTION
# -----------------------------

if page == "Ask Valora":
    st.header("Ask Valora")
    question = st.text_input("Ask something")

    if st.button("Send") and question:
        memories = hindsight.recall(
            bank_id="echoproof",
            query=question
        )
        memory_text: str = "\n".join(
            [memory.text for memory in memories.results]
        )
        if debug_mode:
            st.subheader("Retrieved Memories")
            st.write(memory_text)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"""
    Relevant memories:
    {memory_text}
    User question:
    {question}
    Answer using the memories when relevant
    """
                }
            ]
        )
        answer = response.choices[0].message.content
        st.subheader("AI Response")
        st.write(answer)

# -----------------------------
# INVESTOR INSIGHTS SECTION
# -----------------------------
if page == "Investor Insights":
    st.header("Investor Insights")
    if st.button("Analyze Investor Patterns"):
        memories = hindsight.recall(
            bank_id="echoproof",
            query="investor rejection reasons"
        )
        memory_text = "\n".join(
            [memory.text for memory in memories.results]
        )
        analysis = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    You are a venture capital analyst.
                    Analyze the following investor memories.
                    Find:
                    1. Most common rejection reasons
                    2. Investor patterns
                    3. Key startup weaknesses
                    4. Advice for founders
                    Memories:
                    {memory_text}
"""
            }
        ]
    )
        result = analysis.choices[0].message.content
        st.subheader("Investor Intelligence Report")
        st.write(result)

    # -----------------------------
# STARTUP PITCH PREDICTOR
# -----------------------------
if page == "Startup Pitch Predictor":
    st.header("Startup Pitch Predictor")
    startup_name = st.text_input("Startup Name")
    startup_description = st.text_area(
        "Describe your startup"
        )
    if st.button("Predict Investor Response"):
        memories = hindsight.recall(
            bank_id="echoproof",
            query=startup_description
        )
        memory_text = "\n".join(
            [memory.text for memory in memories.results]
        )
        prediction = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    You are an experienced venture capitalist.
                    Analyze this startup.
                    Startup Name:
                    {startup_name}
                    Startup Description:
                    {startup_description}
                    Relevant investor memories:
                    {memory_text}
                    Give:
                    1. Investor Readiness Score (0-100)
                    2. Top 3 Investor Concerns
                    3. Recommended Improvements
                    4. Funding Outlook
                    Be specific and practical.
                    """
            }
        ]
    )
        prediction_result = (
            prediction.choices[0].message.content
        )
        st.subheader("Investor Prediction Report")
        st.write(prediction_result)

    # -----------------------------
# INVESTOR OUTCOME LOGGER
# -----------------------------
if page == "Investment Outcome Logger":
    st.header("Investor Outcome Logger")
    investor_name = st.text_input(
        "Investor Name"
    )
    startup_name_log = st.text_input(
        "Startup Name (for logging)"
    )
    outcome = st.selectbox(
        "Outcome",
        ["Accepted", "Rejected"]
    )
    reason = st.text_area(
        "Reason"
    )
    if st.button("Save Outcome"):
        memory_content = f"""
        Investor: {investor_name}
        Startup: {startup_name_log}
        Outcome: {outcome}
        Reason: {reason}
"""
        hindsight.retain(
            bank_id="echoproof",
            content=memory_content
        )
        st.success("Outcome saved to memory!")

    # -----------------------------
# SIMILAR STARTUP FINDER
# -----------------------------
if page == "Similar Startup Finder":
    st.header("Similar Startup Finder")
    startup_query = st.text_area(
        "Describe a startup idea"
    )
    if st.button("Find Similar Cases"):
        memories = hindsight.recall(
            bank_id="echoproof",
            query=startup_query
        )
        memory_text = "\n".join(
            [memory.text for memory in memories.results]
        )
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    You are a startup advisor.
                    Startup Idea:
                    {startup_query}
                    Past Investor Memories:
                    {memory_text}
                    Provide:
                    1. Similar startup patterns
                    2. Common investor concerns
                    3. Mistakes founders made
                    4. How to avoid those mistakes
                    5. Success Probability Score (0-100)
                    Be practical and concise.
                    """
            }
        ]
    )
        result = response.choices[0].message.content
        st.subheader("Founder Risk Report")
        st.write(result)

    # -----------------------------
# INVESTOR MATCHMAKER
# -----------------------------
if page =="Investor Matchmaker":
    st.header("Investor Matchmaker")
    match_startup = st.text_area(
        "Describe your startup for investor matching"
    )
    if st.button("Find Best Investors"):
        memories = hindsight.recall(
            bank_id="echoproof",
            query=match_startup
        )
        memory_text = "\n".join(
            [memory.text for memory in memories.results]
            )
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    You are a venture capital expert.
                    Startup Description:
                    {match_startup}
                    Investor Memory Database:
                    {memory_text}
                    Based on past investor behavior:
                    1. Recommend the 5 best investors.
                    2. Recommend investors to avoid.
                    3. Explain why.
                    4. Give fundraising strategy.
                    5. Give overall funding probability (0-100).
                    Be practical and specific.
                    """
            }
        ]
    )
        result = response.choices[0].message.content
        st.subheader("Investor Match Report")
        st.write(result)