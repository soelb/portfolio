import streamlit as st
import spacy

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Mapping of jargon terms to simpler alternatives
jargon_map = {
    "asynchronous": "non-blocking",
    "orchestration": "coordination",
    "microservices": "small services",
    "containerized": "packaged",
    "observability": "monitoring"
}

# Streamlit app UI
st.title("🧪 Jargon Detector")
st.write("Paste technical writing below to detect and simplify complex terms:")

# Text input area
text = st.text_area("📄 Your Text", height=200)

# When the 'Detect Jargon' button is pressed
if st.button("🔍 Detect Jargon"):
    doc = nlp(text)  # Process text using spaCy
    suggestions = []

    # Scan each word for jargon
    for token in doc:
        word = token.text.lower()
        if word in jargon_map:
            suggestions.append(f"**{token.text}** → _{jargon_map[word]}_")

    # Display results
    if suggestions:
        st.markdown("### 🔧 Suggestions:")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")
    else:
        st.success("✅ No complex jargon detected!")
