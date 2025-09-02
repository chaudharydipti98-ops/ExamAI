import streamlit as st
import random

# ---- Page Config ----
st.set_page_config(page_title="ExamAI", page_icon="📘", layout="centered")

st.title("📘 ExamAI")
st.write("Get important board exam questions instantly!")

# ---- Dropdowns ----
class_option = st.selectbox("Select Class", [f"Class {i}" for i in range(6, 13)])
board_option = st.selectbox("Select Board", ["CBSE", "ICSE", "State Board"])
subject_option = st.selectbox(
    "Select Subject",
    ["Maths", "Science", "English", "Hindi", "Social Science"]
)

# ---- Button ----
if st.button("Generate Questions"):
    st.subheader(f"📑 Important Questions for {class_option} - {board_option} - {subject_option}")

    # Dummy questions (replace with AI/DB later if you want)
    sample_questions = [
        "Explain the main concept of this chapter.",
        "Solve the numerical problem from exercise 5.2.",
        "Write short notes on key terms.",
        "Discuss the importance of the topic.",
        "Derive the main formula with steps.",
        "Explain with an example.",
        "List 5 differences between related concepts.",
        "Why is this topic important in real life?",
        "Give a diagram-based explanation.",
        "Summarize the chapter in your own words."
    ]

    random.shuffle(sample_questions)
    for i, q in enumerate(sample_questions, 1):
        st.write(f"**Q{i}. {q}**")
