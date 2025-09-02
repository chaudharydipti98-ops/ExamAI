import streamlit as st
import random

# ----------------------------
# Sample Question Bank (Dummy Data for now)
# In real case, you can expand it with full database or AI API
# ----------------------------
question_bank = {
    "Class 10": {
        "Maths": [
            "Solve: (x + 1)^2 - (x - 1)^2 = ?",
            "Find roots of the quadratic equation 2x² - 3x + 1 = 0",
            "If sin A = 3/5, find cos A",
            "Previous Year Q: A card is drawn from a well-shuffled deck. Find probability of getting a red card.",
            "Word Problem: A train 120 m long passes a pole in 6 seconds. Find its speed in km/hr."
        ],
        "Science": [
            "Define Ohm’s law with formula and SI unit.",
            "Explain Mendeleev’s periodic table with merits and demerits.",
            "Previous Year Q: Write one difference between aerobic and anaerobic respiration.",
            "Word Problem: An electric lamp is connected to 6V battery and draws 0.5 A current. Calculate resistance of lamp.",
            "Give reason: Why is photosynthesis important for survival of life?"
        ]
    },
    "Class 12": {
        "Physics": [
            "State and explain Faraday’s law of electromagnetic induction.",
            "Previous Year Q: Derive expression for drift velocity of electrons.",
            "Numerical: A capacitor of 10 μF is charged by 50 V supply. Calculate energy stored.",
            "Explain working of AC generator with diagram.",
            "Give two applications of semiconductors in daily life."
        ],
        "Chemistry": [
            "Write IUPAC name of CH3CH2COOH.",
            "Differentiate between physisorption and chemisorption.",
            "Previous Year Q: What is the role of cryolite in Hall’s process of extraction of Aluminium?",
            "Numerical: Calculate pH of 0.001 M HCl solution.",
            "State Raoult’s law with mathematical expression."
        ]
    }
}

# ----------------------------
# Streamlit App
# ----------------------------
st.set_page_config(page_title="📘 Board Exam AI", layout="centered")

st.title("📘 Exam Question Generator")
st.write("Get **realistic exam questions** from NCERT / SCERT / State Board + Previous Year Papers!")

# Inputs
class_selected = st.selectbox("Select Class", ["Class 10", "Class 12"])
board_selected = st.selectbox("Select Board", ["CBSE", "ICSE", "State Board", "NCERT", "SCERT"])
subject_selected = st.selectbox("Select Subject", ["Maths", "Science", "Physics", "Chemistry"])
book_name = st.text_input("Enter Book Name (e.g., NCERT Physics Part-1)")

if st.button("Generate Exam Questions"):
    if class_selected in question_bank and subject_selected in question_bank[class_selected]:
        questions = random.sample(question_bank[class_selected][subject_selected], k=5)
        st.subheader("📑 Suggested Exam Questions:")
        for i, q in enumerate(questions, start=1):
            st.write(f"**Q{i}.** {q}")
    else:
        st.error("❌ Sorry! No data available for this selection yet.")
