import streamlit as st

# --- Global Styling (single place for all CSS) ---
st.markdown("""
    <style>
    /* Page Background & Text */
    .stApp {
        background-color: #2d3142;
        color: #eae8ff;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #b0d7ff;
        margin: 0.25rem 0;
    }

    /* Divider */
    hr {
        border-color: #b0d7ff;
    }

    /* Generic blocks used across the site */
    .edu-block, .project-card, .achievement-item, .contact-card {
        background-color: #d8d5db !important;
        color: #2d3142 !important;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        box-sizing: border-box;
    }

    /* Titles inside blocks */
    .edu-title, .project-title {
        color: #2d3142;
        font-weight: 700;
    }

    .edu-details, .project-desc {
        color: #adacb5;
    }

    /* Skill pills */
    .skill-section { margin-top: 25px; margin-bottom: 30px; }
    .skill-title { font-size: 22px; font-weight: 700; margin-bottom: 15px; color: #b0d7ff; }
    .skill-container { display: flex; flex-wrap: wrap; gap: 15px; }
    .skill-pill {
        background-color: #b0d7ff !important;
        color: #2d3142 !important;
        border: 2px solid #2d3142;
        font-weight: 700;
        border-radius: 20px;
        padding: 10px 18px;
        margin: 5px;
        display: inline-block;
        transition: all 0.25s ease;
        min-width: 120px;
        text-align: center;
    }
    .skill-pill:hover {
        background-color: #2d3142 !important;
        color: #b0d7ff !important;
        transform: scale(1.05);
        cursor: pointer;
    }

    /* Inputs & Textareas */
    input, textarea, .stTextInput>div>input, .stTextArea>div>textarea {
        background-color: #eae8ff !important;
        color: #2d3142 !important;
        border: 2px solid #2d3142 !important;
        border-radius: 8px;
        padding: 10px !important;
        font-size: 16px;
    }
    input:focus, textarea:focus, .stTextInput>div>input:focus, .stTextArea>div>textarea:focus {
        border-color: #b0d7ff !important;
        outline: none !important;
        box-shadow: 0 0 6px #b0d7ff;
    }

    
    /* === Unified Button Styling (applies to all button types) === */
    .stButton > button,
    .stFormSubmitButton > button,
    .stDownloadButton > button {
        background-color: #b0d7ff !important; /* pale blue background */
        color: #2d3142 !important;           /* dark text */
        border-radius: 8px;                  /* rounded corners */
        border: 2px solid #2d3142;           /* dark border */
        font-weight: 800;                    /* bold text */
        font-size: 16px;                     /* medium-large font */
        padding: 8px 20px;                   /* roomy click area */
        transition: background-color 0.25s ease,
                    color 0.25s ease,
                    border-color 0.25s ease,
                    transform 0.25s ease,
                    box-shadow 0.25s ease;   /* smooth hover animations */
}

    .stButton > button:hover,
    .stFormSubmitButton > button:hover,
    .stDownloadButton > button:hover {
        background-color: #2d3142 !important; /* invert background */
        color: #b0d7ff !important;            /* invert text */
        border: 2px solid #b0d7ff;            /* invert border */
        transform: scale(1.03);               /* slight grow effect */
        box-shadow: 0px 4px 10px rgba(0,0,0,0.25); /* subtle shadow */
}


    /* Project cards */
    .project-card {
        background-color: #f9f9f9 !important;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.08);
        transition: 0.2s ease-in-out;
    }
    .project-card:hover {
        transform: translateY(-4px) scale(1.01);
        box-shadow: 0 8px 18px rgba(0,0,0,0.12);
    }
    .project-title { font-size: 18px; font-weight: 700; margin-bottom: 5px; }
    .project-desc { font-size: 15px; color: #444; line-height: 1.5; }

    /* Achievements list */
    .achievement-list { display: flex; flex-direction: column; gap: 10px; margin-top: 15px; }
    .achievement-item {
        background-color: #eef5ff !important;
        padding: 12px;
        border-radius: 8px;
        font-size: 15px;
        font-weight: 500;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }

    /* Contact cards */
    .contact-section { display: flex; flex-wrap: wrap; gap: 20px; margin-top: 20px; }
    .contact-card {
        background-color: #b0d7ff !important;
        color: #2d3142 !important;
        padding: 20px;
        border-radius: 12px;
        flex: 1 1 200px;
        min-width: 200px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.12);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        text-align: center;
    }
    .contact-card:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0,0,0,0.22);
        cursor: pointer;
    }
    .contact-icon { font-size: 24px; margin-bottom: 10px; }
    .contact-title { font-weight: 700; font-size: 16px; margin-bottom: 5px; }
    .contact-link { color: #2d3142; text-decoration: none; word-break: break-all; }
    .contact-link:hover { text-decoration: underline; }

    /* Form alert look */
    .stAlert {
        border-radius: 8px;
        padding: 10px;
        font-weight: 600;
        max-width: 600px;
        margin: 15px auto;
        color: #2d3142;
        background-color: #eae8ff;
        border: 2px solid #b0d7ff;
    }

    /* Small responsiveness tweaks */
    @media (max-width: 800px) {
        .skill-pill { min-width: 100px; padding: 8px 12px; font-size: 14px; }
        .stDownloadButton > button, .stButton > button { font-size: 14px; padding: 6px 14px; }
        .contact-card { min-width: 150px; }
    }
    </style>
""", unsafe_allow_html=True)

# Page Configuration
st.set_page_config(page_title="Shakshi's Portfolio", page_icon='👨‍💻', layout='wide')

# Create two columns
col1, col2 = st.columns([2, 1])  # First column 2x wider than second column

with col1:
    st.title("Hi, I'm Shakshi Khambhayata")
    st.subheader("AI/ML Engineer | Data Scientist | Python Enthusiast")
    st.write("Welcome to my portfolio website! Here you can learn about who I really am.")

    # Resume Download Button
    with open("assets/Shakshi's Resume.pdf", "rb") as file:
        st.download_button("Download My Resume", data=file, file_name="Shakshi_Resume.pdf", mime="application/pdf")

with col2:
    st.image("assets/Shakshi's updated photo.png", width=500)


st.title("👩‍💻 About Me")
# --- Small Summary ---
st.markdown("""
<p style="font-size:18px; line-height:1.6;">
I am a <b>Computer Engineering student</b> passionate about Python, Machine Learning, and emerging technologies.
I enjoy coding, problem-solving, and building data-driven projects.  
Here is a detailed look at my background and experience:
</p>
""", unsafe_allow_html=True)

st.markdown("---")  # Divider

# --- Education Section ---
st.subheader("🎓 Education")

# Education HTML (no inline CSS here — uses classes defined in global CSS)
st.markdown("""
<div class="edu-block">
    <div>
        <div class="edu-title">B.E. Computer Engineering</div>
        <div class="edu-details">V.V.P. Engineering College (2022 - 2026)</div>
    </div>
    <div class="edu-marks">CPI: 8.91</div>
</div>

<div class="edu-block">
    <div>
        <div class="edu-title">Higher Secondary</div>
        <div class="edu-details">Tapasvi School, Rajkot (2020 - 2022)</div>
    </div>
    <div class="edu-marks">Percentage: 72%</div>
</div>

<div class="edu-block">
    <div>
        <div class="edu-title">Primary & Secondary Education</div>
        <div class="edu-details">St. Mary’s School, Rajkot (2013 - 2020)</div>
    </div>
    <div class="edu-marks">Percentage: 82%</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")  # Divider

# --- Skills Section ---
st.subheader("🛠 Skills")

st.markdown("<div class='skill-section'><div class='skill-title'>Programming Languages</div>", unsafe_allow_html=True)
st.markdown("""
<div class="skill-container">
    <div class="skill-pill">Python</div>
    <div class="skill-pill">Java</div>
    <div class="skill-pill">C</div>
</div></div>
""", unsafe_allow_html=True)

st.markdown("<div class='skill-section'><div class='skill-title'>Libraries</div>", unsafe_allow_html=True)
st.markdown("""
<div class="skill-container">
    <div class="skill-pill">NumPy</div>
    <div class="skill-pill">Pandas</div>
    <div class="skill-pill">Matplotlib</div>
    <div class="skill-pill">Seaborn</div>
    <div class="skill-pill">Scikit-Learn</div>
    <div class="skill-pill">TensorFlow</div>
</div></div>
""", unsafe_allow_html=True)

st.markdown("<div class='skill-section'><div class='skill-title'>Frontend</div>", unsafe_allow_html=True)
st.markdown("""
<div class="skill-container">
    <div class="skill-pill">streamlit</div>
    <div class="skill-pill">HTML</div>
    <div class="skill-pill">CSS</div>
    <div class="skill-pill">Javascript</div>
</div></div>
""", unsafe_allow_html=True)

st.markdown("<div class='skill-section'><div class='skill-title'>Backend</div>", unsafe_allow_html=True)
st.markdown("""
<div class="skill-container">
    <div class="skill-pill">Flask</div>
    <div class="skill-pill">Fastapi</div>
</div></div>
""", unsafe_allow_html=True)

st.markdown("<div class='skill-section'><div class='skill-title'>Database & OS</div>", unsafe_allow_html=True)
st.markdown("""
<div class="skill-container">
    <div class="skill-pill">MySQL</div>
    <div class="skill-pill">Linux</div>
</div></div>
""", unsafe_allow_html=True)

st.markdown("<div class='skill-section'><div class='skill-title'>Tools</div>", unsafe_allow_html=True)
st.markdown("""
<div class="skill-container">
    <div class="skill-pill">Google Colab</div>
    <div class="skill-pill">Jupyter</div>
    <div class="skill-pill">Krita</div>
    <div class="skill-pill">Tableau</div>
    <div class="skill-pill">GitHub</div>
</div></div>
""", unsafe_allow_html=True)

st.markdown("<div class='skill-section'><div class='skill-title'>Soft Skills</div>", unsafe_allow_html=True)
st.markdown("""
<div class="skill-container">
    <div class="skill-pill">Problem Solving</div>
    <div class="skill-pill">Creative Thinking</div>
    <div class="skill-pill">Critical Thinking</div>
    <div class="skill-pill">Communication</div>
</div></div>
""", unsafe_allow_html=True)


# --- Projects Section ---
st.subheader("📂 Projects")

# Project cards use .project-card / .project-title / .project-desc classes from global CSS
st.markdown("""
<div class="project-card">
    <div class="project-title">📊 Data Analysis on McDonald's Financial Statements</div>
    <div class="project-desc">
        Cleaned and processed dataset with Pandas, used NumPy for statistics, and visualized patterns with Matplotlib. 
        Analyzed correlations, trends, and outliers to generate insights.
    </div>
</div>

<div class="project-card">
    <div class="project-title">🎨 Style Transfer Generation Model</div>
    <div class="project-desc">
        Developed an image style transfer project using TensorFlow Hub's pre-trained models to apply 
        the artistic style of one image to another. Visualized results with Matplotlib.
    </div>
</div>

<div class="project-card">
    <div class="project-title">🤟 Sign Language Digits Prediction Model</div>
    <div class="project-desc">
        Built a CNN-based model to classify digits (0–9) from hand gesture images in real-time using OpenCV and Keras. 
        Preprocessed images, applied data augmentation, and achieved high accuracy.
    </div>
</div>
""", unsafe_allow_html=True)

# --- Achievements Section ---
st.subheader("🏆 Achievements & Leadership")
st.markdown("""
<div class="achievement-list">
    <div class="achievement-item">📝 Wrote a research paper about Cyber Security</div>
    <div class="achievement-item">🏀 National-Level Basketball Player</div>
    <div class="achievement-item">🎯 AIR 140 in NID 2022 (National Institute of Design)</div>
    <div class="achievement-item">🎨 Fine Arts Club Coordinator in College</div>
    <div class="achievement-item">📐 Lead Coordinator for School Decoration Team</div>
</div>
""", unsafe_allow_html=True)


# --- Contact Section ---
st.markdown("---")
st.subheader("📬 Contact Me")

with st.form("contact_form", clear_on_submit=True):
    st.subheader("Name : ")
    name = st.text_input("Your Name")
    st.subheader("Email : ")
    email = st.text_input("Your Email")
    st.subheader("Message : ")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send Message")

    if submitted:
        if name and email and message:
            st.success(f"✅ Thank you {name}, your message has been submitted!")
        else:
            st.error("⚠️ Please fill out all fields before submitting.")


# Contact Cards (no inline styles — use the global classes)
st.markdown("""
<div class="contact-section">
    <div class="contact-card">
        <div class="contact-icon">📧</div>
        <div class="contact-title">Email</div>
        <a class="contact-link" href="mailto:2124shakshi@gmail.com">2124shakshi@gmail.com</a>
    </div>
    <div class="contact-card">
        <div class="contact-icon">📱</div>
        <div class="contact-title">Phone</div>
        <div class="contact-link">+91 88495 50350</div>
    </div>
    <div class="contact-card">
        <div class="contact-icon">🔗</div>
        <div class="contact-title">LinkedIn</div>
        <a class="contact-link" href="https://www.linkedin.com/in/shakshi-khambhayata-/" target="_blank">View Profile</a>
    </div>
    <div class="contact-card">
        <div class="contact-icon">🖥️</div>
        <div class="contact-title">GitHub</div>
        <a class="contact-link" href="https://github.com/shakshi-7" target="_blank">View Projects</a>
    </div>
</div>
""", unsafe_allow_html=True)
