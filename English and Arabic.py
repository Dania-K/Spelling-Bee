import streamlit as st
import random

# Define word lists for each grade and language
word_lists = {
    "English": {
        "Grade1": ["adventure", "hill", "shirt", "black", "house"],
        "Grade2": ["africa", "curiosity", "mirror", "dresser", "palestine"],
        "Grade3": ["apartment", "illuminate", "numbers", "backpack", "invent"],
        "Grade4": ["ambiguous", "giraffe", "percentage", "antarctic", "glamorous"],
        "Grade5": ["abdicate", "eccentricity", "perpendicular", "accommodate", "evaporate"],
        "Grade6": ["administration", "ephemeral", "mischievous", "advanced", "esoteric"],
        "Grade7": ["accompany", "enlisted", "perspicacity", "affirmation", "euphoria"],
        "Grade8": ["adage", "detrimental", "onomatopoeia", "affirmation", "dexterity"],
    },
    "Arabic": {
        "Grade1": ["بيت", "مدرسة", "شجرة", "قلم", "كتاب"],
        "Grade2": ["معلم", "طلاب", "طاولة", "باب", "نافذة"],
        "Grade3": ["مدينة", "شارع", "قطار", "مكتبة", "حافلة"],
        "Grade4": ["جسر", "مستشفى", "حديقة", "سفينة", "طيارة"],
        "Grade5": ["مفتاح", "كرسي", "هاتف", "حاسوب", "ساعة"],
        "Grade6": ["سيارة", "مصنع", "مطار", "ميناء", "قلعة"],
        "Grade7": ["قمر", "شمس", "نجم", "سحاب", "ريح"],
        "Grade8": ["كهف", "جبل", "غابة", "نهر", "بحر"],
    },
}

# Initialize session state
if "used_words" not in st.session_state:
    st.session_state["used_words"] = {lang: {grade: [] for grade in word_lists[lang]} for lang in word_lists}
if "round" not in st.session_state:
    st.session_state["round"] = {lang: {grade: 1 for grade in word_lists[lang]} for lang in word_lists}
if "round_history" not in st.session_state:
    st.session_state["round_history"] = {lang: {grade: {} for grade in word_lists[lang]} for lang in word_lists}

# Sidebar for language and grade selection
selected_language = st.sidebar.radio("Select Language:", options=list(word_lists.keys()))
selected_grade = st.sidebar.selectbox("Select Grade:", options=list(word_lists[selected_language].keys()))

# App title
st.title(f"{selected_language} Spelling Bee")
st.write("Manage your spelling bee competition with ease!")

# Input for number of contestants
num_contestants = st.number_input("Enter number of contestants:", min_value=1, step=1)

# Assign words for the current round
if st.button("Assign Words"):
    available_words = [
        word for word in word_lists[selected_language][selected_grade]
        if word not in st.session_state["used_words"][selected_language][selected_grade]
    ]

    if len(available_words) >= num_contestants:
        assigned_words = random.sample(available_words, num_contestants)
        st.session_state["used_words"][selected_language][selected_grade].extend(assigned_words)

        current_round = st.session_state["round"][selected_language][selected_grade]
        st.session_state["round_history"][selected_language][selected_grade][current_round] = assigned_words

        st.success(f"Round {current_round} Words Assigned:")
        for i, word in enumerate(assigned_words, start=1):
            st.write(f"Contestant {i}: {word}")
    else:
        st.warning("Not enough words available. Reduce the number of contestants.")

# Display round history
st.subheader("Round History")
for round_number, words in st.session_state["round_history"][selected_language][selected_grade].items():
    st.write(f"Round {round_number}: {', '.join(words)}")

# Progress to the next round
if st.button("Next Round"):
    st.session_state["round"][selected_language][selected_grade] += 1
    st.success(f"Proceeding to Round {st.session_state['round'][selected_language][selected_grade]}.")
