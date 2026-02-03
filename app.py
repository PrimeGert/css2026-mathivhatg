import streamlit as st
import pandas as pd
import plotly.express as px

#  Page Config 
st.set_page_config(
    page_title="Thilivhali Mathivha's Professional Profile",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Mode Toggle

# Initialize session state
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Sidebar toggle
st.sidebar.markdown("### Appearance")
st.session_state.dark_mode = st.sidebar.toggle(
    "Dark mode",
    value=st.session_state.dark_mode
)

# Apply dark mode styles conditionally
if st.session_state.dark_mode:
    st.markdown(
        """
        <style>
        /* Main app background */
        .stApp {
            background-color: #0e1117;
            color: #fafafa;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #161b22;
        }

        /* Headers */
        h1, h2, h3, h4 {
            color: #fafafa;
        }

        /* Text */
        p, span, label {
            color: #e6edf3;
        }

        /* Metrics */
        div[data-testid="metric-container"] {
            background-color: #161b22;
            border-radius: 10px;
            padding: 10px;
        }

        /* Buttons */
        button {
            background-color: #238636;
            color: white;
            border-radius: 8px;
        }

        /* Links */
        a {
            color: #58a6ff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

#  Sidebar 
st.sidebar.title("Thilivhali Mathivha")
st.sidebar.caption("Junior Lecturer • Data Scientist")

menu = st.sidebar.radio(
    "Navigate",
    ["About Me", "Skills", "Experience", "Education",  "Contact"]
)

# Header 
st.markdown(
    """
    <h1 style='text-align:center;'>Thilivhali Mathivha</h1>
    <p style='text-align:center; font-size:18px;'>
    Junior Lecturer | Data Science | Applied Mathematics </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# About Me
if menu == "About Me":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Personal Statement")
        st.write(
            """
            I am a self-motivated individual with strong coding, communication, and interpersonal skills.
            I thrive under pressure, work effectively both independently and in teams, and maintain a keen eye for detail.

            My professional focus lies at the intersection of **applied mathematics and data science**,
            with a strong passion for teaching, mentoring, and research-driven problem solving.
            """
        )

    with col2:
        st.metric("Experience", "3+ Years")
        st.metric("Teaching", "University Level")
        st.metric("Primary Focus", "Mathematics")

# Skills
elif menu == "Skills":
    
    st.subheader("Technology Stack")

    skills = {
        "Python": 75,
        "MATLAB": 70,
        "Git/GitHub": 30,
        "PostgreSQL": 85,
        "Machine Learning": 65
    }

    df_skills = pd.DataFrame({
        "Skill": list(skills.keys()),
        "Proficiency": list(skills.values())
    })

    fig = px.bar(
        df_skills,
        x="Proficiency",
        y="Skill",
        orientation="h",
        title="Skill Proficiency Overview",
        range_x=[0, 100]
    )

    st.plotly_chart(fig, use_container_width=True)

# Experience
elif menu == "Experience":
    st.subheader("Work Experience")

    experience = [
        ("Junior Lecturer", "University of Venda", "2022 – Present"),
        ("Mathematics Tutor", "Varsity Mathsiah Online", "2021"),
        ("Research Assistant", "University of Venda", "2019"),
        ("Mathematics Tutor", "University of Venda", "2018")
    ]

    for role, org, period in experience:
        with st.container():
            st.markdown(f"### {role}")
            st.markdown(f"**{org}**  ")
            st.caption(period)
            st.divider()

# Education
elif menu == "Education":
    st.subheader("Education")

    education = [
        ("WorldQuant University", "Certificate in Data Science with Python (Honours)"),
        ("University of Venda", "BSc Honours in Applied Mathematics (Distinction)"),
        ("University of Venda", "BSc in Computer Science & Mathematics (Distinction)")
    ]

    for uni, degree in education:
        st.markdown(f"### {degree}")
        st.markdown(f"**{uni}** ")
        st.divider()


# Contact

elif menu == "Contact":
    st.subheader("Contact Information")

    st.markdown("""
    **📧 Email:** mathstgg@gmail.com  
    **📞 Phone:** 082 867 5067 / 073 203 7786  
    **🌍 Location:** South Africa
    """)
