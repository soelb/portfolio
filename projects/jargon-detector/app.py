import streamlit as st
import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Jargon mapping
jargon_map = {
    "asynchronous": "non-blocking",
    "orchestration": "coordination",
    "microservices": "small services",
    "containerized": "packaged",
    "observability": "monitoring"
}

# App UI
st.title("🧪 Jargon Detector")
st.write("Paste technical writing below to detect and simplify complex terms:")

text = st.text_area("📄 Your Text", height=200)

if st.button("🔍 Detect Jargon"):
    doc = nlp(text)
    suggestions = []
    for token in doc:
        word = token.text.lower()
        if word in jargon_map:
            suggestions.append(f"**{token.text}** → _{jargon_map[word]}_")
    
    if suggestions:
        st.markdown("### 🔧 Suggestions:")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")
    else:
        st.success("✅ No complex jargon detected!")
