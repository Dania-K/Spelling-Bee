import streamlit as st
import random

# Define word lists for each grade
word_lists = {
    "Grade1": [
        "adventure", "hill", "shirt", "black", "house", "stem",
        "brown", "king", "butterfly", "lad", "carpet", "leaves",
        "three", "cereal", "love", "wear", "elephant", "week",
        "flower", "pants", "white", "game", "paper", "yard",
        "grapes", "purple", "yellow", "green", "rain", "yelp",
        "happy", "rainbow", "agile"
    ],
    "Grade2": [
        "africa", "curiosity", "mirror", "after", "dresser", "palestine",
        "amharic", "eight", "playground", "english", "precious",
        "bangladesh", "ethiopia", "radiant", "bathroom", "europe", "rectangle",
        "bird", "familiar", "school", "blanket", "find", "spanish",
        "bookcase", "flower", "square", "books", "gratitude", "symphony",
        "canada", "hindi", "temperature", "carpet", "laugh", "urdu",
        "ceiling", "mean", "write", "click"
    ],
    "Grade3": [
        "apartment", "illuminate", "numbers", "backpack", "invent", "nutmeg",
        "bicycle", "jellyfish", "octopus", "boxcar", "kitchen", "peculiar",
        "butterfly", "language", "perseverance", "camera", "latch", "plaster",
        "chalkboard", "lessons", "poached", "complex", "letters", "pumpkin",
        "daring", "library", "rabbit", "delicate", "loaf", "school",
        "division", "meaning", "telescope", "dreamers", "microscope", "umbrella",
        "encyclopedia", "monkey", "violin", "favorite", "multiplication", "waterfall",
        "guitar", "mysterious", "xylophone"
    ],
    "Grade4": [
        "ambiguous", "giraffe", "percentage", "antarctic", "glamorous", "phenomenal",
        "calendar", "graduate", "presentation", "centipede", "guess", "question",
        "conscientious", "handwriting", "recent", "counsel", "hardship", "refrigerator",
        "coupon", "helicopter", "rough", "crackle", "highlight", "sincere",
        "custard", "igloo", "spreadsheet", "darkness", "ingenious", "stampede",
        "demonstrate", "jaguar", "suitable", "devastate", "kangaroo", "swordsmen",
        "dinosaur", "medication", "vikings", "dither", "nightmare", "windshield",
        "essential", "norsemen", "wishful", "exchange", "opportunity", "wristwatch",
        "exquisite", "ostrich"
    ],
    "Grade5": [
        "abdicate", "eccentricity", "perpendicular", "accommodate", "evaporate",
        "predominant", "advanced", "evermore", "quagmire", "ambiguous", "extensive",
        "qualitative", "amusing", "formidable", "solution", "barrage", "gigantic",
        "solvent", "belligerent", "gregarious", "berserk", "hypnotize", "squeeze",
        "bizarre", "incognito", "translucent", "bureaucracy", "intersect", "tuneful",
        "cabbage", "intuition", "ubiquitous", "complementary", "knelt", "unwavering",
        "confiscate", "leopard", "vanish", "construction", "meticulous", "versatile",
        "continuous", "nauseate", "violet", "creatures", "nostalgic", "voice",
        "dehydrated", "optimistic", "whimsical", "derogatory", "oscillate"
    ],
    "Grade6": [
        "administration", "ephemeral", "mischievous", "advanced", "esoteric", "negotiation",
        "alabaster", "exterior", "partisan", "altitude", "facetious", "phenomenon",
        "amiable", "faucet", "primers", "amusing", "garrulous", "procession",
        "anthem", "hexagonal", "pronounce", "banishment", "hypothesis", "recognition",
        "barricade", "improvise", "reimburse", "boisterous", "inscrutable", "relics",
        "commemorate", "intrepid", "resemble", "compliant", "jubilation", "salvation",
        "conclusion", "kaleidoscope", "scrimmage", "conference", "kneel", "simulation",
        "conserve", "leadership", "spectators", "discomfort", "lecture", "strident",
        "disengage", "leeway", "subdivision", "disseminate", "luminance", "vagabond"
    ],
    "Grade7": [
        "accompany", "enlisted", "perspicacity", "affirmation", "euphoria", "pharaoh",
        "alabaster", "fluctuate", "quaim", "altitude", "germinate", "quantum",
        "brigadier", "inexorable", "recognition", "bulletin", "infraction", "resourceful",
        "cherished", "jettison", "sausage", "collaboration", "lascivious", "scenery",
        "colonel", "lieutenant", "scrimmage", "commendable", "mellfluous", "siesta",
        "commissioned", "sophomore", "composure", "miniature", "stagnant", "conquering",
        "miracle", "superfluous", "consecutive", "narration"
    ],
    "Grade8": [
        "adage", "detrimental", "onomatopoeia", "affirmation", "dexterity", "perfidious",
        "airman", "discordant", "piedmont", "amethyst", "discredit", "plaudits",
        "amphitheater", "discrepancy", "preclude", "annexation", "disparate", "pronunciation",
        "appendectomy", "pulmonary", "azalea", "ephemeral", "auaint", "boisterously",
        "excerpt", "auixotic", "cacophony", "extravaganza", "redundancy", "chandeliers",
        "handkerchief", "remorse", "cherished", "indelible", "servile", "churlish",
        "indigenous", "sobriety", "cinnabar", "jubilee", "sphinx"
    ]
}

# Initialize state to track used words, contestants, and rounds
if "used_words" not in st.session_state:
    st.session_state["used_words"] = {grade: [] for grade in word_lists.keys()}
if "contestants" not in st.session_state:
    st.session_state["contestants"] = {grade: [] for grade in word_lists.keys()}
if "round" not in st.session_state:
    st.session_state["round"] = {grade: 1 for grade in word_lists.keys()}
if "round_history" not in st.session_state:
    st.session_state["round_history"] = {grade: {} for grade in word_lists.keys()}

# Streamlit app title
st.markdown("""<style>
h1 {
    color: #2b6cb0;
    font-family: 'Arial';
    text-align: left;
    margin-bottom: 20px;
}
</style>
<h1>📝 MD Tutorials: 3rd Annual Spelling Bee Competition</h1>
""", unsafe_allow_html=True)

# Add an app description
st.markdown("""
<div style="font-family: Arial; font-size: 16px; margin-bottom: 30px;">
    This application streamlines organizing and managing a spelling bee competition. Select a grade, register contestants, and randomly assign words for each round.
</div>
""", unsafe_allow_html=True)

# Sidebar for grade and customization
st.sidebar.header("Customize Spelling Bee")
selected_grade = st.sidebar.selectbox("Select Grade:", options=list(word_lists.keys()))
st.sidebar.markdown("""<div style="font-size: 14px;">
You can reset the game or customize the rounds here.
</div>""", unsafe_allow_html=True)

# Input number of contestants
st.subheader("Setup Contestants")
st.markdown("Enter the number of contestants for the selected grade.")
num_contestants = st.number_input("Number of contestants:", min_value=1, step=1, key="contestants_input")

# Assign words for the current round
if st.button("Assign Words for Current Round"):
    available_words = [
        word for word in word_lists[selected_grade] 
        if word not in st.session_state["used_words"][selected_grade]
    ]

    if len(available_words) >= num_contestants:
        assigned_words = random.sample(available_words, num_contestants)
        st.session_state["used_words"][selected_grade].extend(assigned_words)
        st.session_state["contestants"][selected_grade] = assigned_words

        # Save to round history
        current_round = st.session_state["round"][selected_grade]
        st.session_state["round_history"][selected_grade][current_round] = assigned_words

        st.success(f"Round {current_round} Words Assigned:")
        for i, word in enumerate(assigned_words, start=1):
            st.write(f"Contestant {i}: {word}")
    else:
        st.warning("Not enough words available to assign to all contestants.")

# Display round history
st.subheader("Round History")
if selected_grade in st.session_state["round_history"]:
    for round_number, words in st.session_state["round_history"][selected_grade].items():
        st.markdown(f"<div style='margin-bottom: 10px;'><strong>Round {round_number}:</strong> {', '.join(words)}</div>", unsafe_allow_html=True)

# Progress to the next round
if st.button("Next Round"):
    st.session_state["round"][selected_grade] += 1
    st.info(f"Moved to Round {st.session_state['round'][selected_grade]}.")

# Reset words, contestants, and rounds
if st.sidebar.button("Reset"):
    st.session_state["used_words"] = {grade: [] for grade in word_lists.keys()}
    st.session_state["contestants"] = {grade: [] for grade in word_lists.keys()}
    st.session_state["round"] = {grade: 1 for grade in word_lists.keys()}
    st.session_state["round_history"] = {grade: {} for grade in word_lists.keys()}
    st.sidebar.success("Game has been reset.")

import streamlit as st
import random

# Arabic word lists for each grade
arabic_word_lists = {
    "Grade1": ["الحمد", "لله", "رب", "العالمين", "الرحمن", "الرحيم", "مالك", "يوم", "الدين", "إياك", "نعبد", "وإياك", "نستعين", "اهدنا", "الصراط", "المستقيم", "صراط", "الذين", "أنعمت", "عليهم", "غير", "المغضوب", "عليهم", "ولا", "الضالين"],
    "Grade2": ["قل", "أعوذ", "برب", "الفلق", "من", "شر", "ما", "خلق", "ومن", "شر", "غاسق", "إذا", "وقب", "ومن", "شر", "النفاثات", "في", "العقد", "ومن", "شر", "حاسد", "إذا", "حسد", "قل", "أعوذ", "برب", "الناس", "ملك", "الناس", "إله", "الناس", "من", "شر", "الوسواس", "الخناس", "الذي", "يوسوس", "في", "صدور", "الناس", "من", "الجنة", "والناس"],
    "Grade3": ["تبت", "يدا", "أبي", "لهب", "وتب", "ما", "أغنى", "عنه", "ماله", "وما", "كسب", "سيصلى", "نارًا", "ذات", "لهب", "وامرأته", "حمالة", "الحطب", "في", "جيدها", "حبل", "من", "مسد", "قل", "هو", "الله", "أحد", "الله", "الصمد", "لم", "يلد", "ولم", "يولد", "ولم", "يكن", "له", "كفوًا", "أحد"],
    "Grade4": ["قل", "يا", "أيها", "الكافرون", "لا", "أعبد", "ما", "تعبدون", "ولا", "أنتم", "عابدون", "ما", "أعبد", "ولا", "أنا", "عابد", "ما", "عبدتم", "لكم", "دينكم", "ولي", "ديني", "إذا", "جاء", "نصر", "الله", "والفتح", "ورأيت", "الناس", "يدخلون", "في", "دين", "الله", "أفواجًا", "فسبح", "بحمد", "ربك", "واستغفره", "إنه", "كان", "توابًا"],
    "Grade5": ["أرأيت", "الذي", "يكذب", "بالدين", "فذلك", "الذي", "يدع", "اليتيم", "ولا", "يحض", "على", "طعام", "المسكين", "فويل", "للمصلين", "الذين", "هم", "عن", "صلاتهم", "ساهون", "الذين", "هم", "يراءون", "ويمنعون", "الماعون", "إنا", "أعطيناك", "الكوثر", "فصل", "لربك", "وانحر", "إن", "شانئك", "هو", "الأبتر"],
    "Grade6": ["ألم", "تر", "كيف", "فعل", "ربك", "بأصحاب", "الفيل", "ألم", "يجعل", "كيدهم", "في", "تضليل", "وأرسل", "عليهم", "طيرًا", "أبابيل", "ترميهم", "بحجارة", "من", "سجيل", "فجعلهم", "كعصف", "مأكول", "لإيلاف", "قريش", "إيلافهم", "رحلة", "الشتاء", "والصيف", "فليعبدوا", "رب", "هذا", "البيت", "الذي", "أطعمهم", "من", "جوع", "وآمنهم", "من", "خوف"],
    "Grade7": ["والعصر", "إن", "الإنسان", "لفي", "خسر", "إلا", "الذين", "آمنوا", "وعملوا", "الصالحات", "وتواصوا", "بالحق", "وتواصوا", "بالصبر", "ويل", "لكل", "همزة", "لمزة", "الذي", "جمع", "مالًا", "وعدده", "يحسب", "أن", "ماله", "أخلده", "كلا", "لينبذن", "في", "الحطمة", "وما", "أدراك", "ما", "الحطمة", "نار", "الله", "الموقدة", "التي", "تطلع", "على", "الأفئدة", "إنها", "عليهم", "مؤصدة", "في", "عمود", "ممددة"],
    "Grade8": ["القارعة", "ما", "القارعة", "وما", "أدراك", "ما", "القارعة", "يوم", "يكون", "الناس", "كالفراش", "المبثوث", "وتكون", "الجبال", "كالعهن", "المنفوش", "فأما", "من", "ثقلت", "موازينه", "فهو", "في", "عيشة", "راضية", "وأما", "من", "خفت", "موازينه", "فأمه", "هاوية", "وما", "أدراك", "ما", "هيه", "نار", "حامية", "ألهاكم", "التكاثر", "حتى", "زرتم", "المقابر", "كلا", "سوف", "تعلمون", "ثم", "كلا", "سوف", "تعلمون", "كلا", "لو", "تعلمون", "علم", "اليقين", "لترون", "الجحيم", "ثم", "لترونها", "عين", "اليقين", "ثم", "لتسألن", "يومئذ", "عن", "النعيم"]
}

# Initialize state to track used words, contestants, and rounds
if "used_words" not in st.session_state:
    st.session_state["used_words"] = {grade: [] for grade in arabic_word_lists.keys()}
if "contestants" not in st.session_state:
    st.session_state["contestants"] = {grade: [] for grade in arabic_word_lists.keys()}
if "round" not in st.session_state:
    st.session_state["round"] = {grade: 1 for grade in arabic_word_lists.keys()}
if "round_history" not in st.session_state:
    st.session_state["round_history"] = {grade: {} for grade in arabic_word_lists.keys()}

# Streamlit app title
st.markdown("""<style>
h1 {
    color: #2b6cb0;
    font-family: 'Arial';
    text-align: left;
    margin-bottom: 20px;
}
</style>
<h1>📝 MD Tutorials: 3rd Annual Arabic Spelling Bee Competition</h1>
""", unsafe_allow_html=True)

# Add an app description
st.markdown("""
<div style="font-family: Arial; font-size: 16px; margin-bottom: 30px;">
    This application streamlines organizing and managing an Arabic spelling bee competition. Select a grade, register contestants, and randomly assign words for each round.
</div>
""", unsafe_allow_html=True)

# Sidebar for grade and customization
st.sidebar.header("Customize Arabic Spelling Bee")
selected_grade = st.sidebar.selectbox("Select Grade:", options=list(arabic_word_lists.keys()))
st.sidebar.markdown("""<div style="font-size: 14px;">
You can reset the game or customize the rounds here.
</div>""", unsafe_allow_html=True)

# Input number of contestants
st.subheader("Setup Contestants")
st.markdown("Enter the number of contestants for the selected grade.")
num_contestants = st.number_input("Number of contestants:", min_value=1, step=1, key="contestants_input")

# Assign words for the current round
if st.button("Assign Words for Current Round"):
    available_words = [
        word for word in arabic_word_lists[selected_grade] 
        if word not in st.session_state["used_words"][selected_grade]
    ]

    if len(available_words) >= num_contestants:
        assigned_words = random.sample(available_words, num_contestants)
        st.session_state["used_words"][selected_grade].extend(assigned_words)
        st.session_state["contestants"][selected_grade] = assigned_words

        # Save to round history
        current_round = st.session_state["round"][selected_grade]
        st.session_state["round_history"][selected_grade][current_round] = assigned_words

        st.success(f"Round {current_round} Words Assigned:")
        for i, word in enumerate(assigned_words, start=1):
            st.write(f"Contestant {i}: {word}")
    else:
        st.warning("Not enough words available to assign to all contestants.")

# Display round history
st.subheader("Round History")
if selected_grade in st.session_state["round_history"]:
    for round_number, words in st.session_state["round_history"][selected_grade].items():
        st.markdown(f"<div style='margin-bottom: 10px;'><strong>Round {round_number}:</strong> {', '.join(words)}</div>", unsafe_allow_html=True)

# Progress to the next round
if st.button("Next Round"):
    st.session_state["round"][selected_grade] += 1
    st.info(f"Moved to Round {st.session_state['round'][selected_grade]}.")

# Reset words, contestants, and rounds
if st.sidebar.button("Reset"):
    st.session_state["used_words"] = {grade: [] for grade in arabic_word_lists.keys()}
    st.session_state["contestants"] = {grade: [] for grade in arabic_word_lists.keys()}
    st.session_state["round"] = {grade: 1 for grade in arabic_word_lists.keys()}
    st.session_state["round_history"] = {grade: {} for grade in arabic_word_lists.keys()}
    st.sidebar.success("Game has been reset.")
