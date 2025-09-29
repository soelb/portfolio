# app.py

import streamlit as st
from coach import explain_term

st.title("🧠 Clarity Coach")
st.write("Paste your technical writing below. We'll flag confusing terms and explain them.")

text = st.text_area("✍️ Enter text here:", height=200)

if st.button("🔍 Explain Jargon"):
    words = text.split()
    results = []
    for word in words:
        result = explain_term(word)
        if result:
            results.append(f"**{word}** → _{result['replacement']}_ \n> {result['explanation']}")
    
    if results:
        st.markdown("### 💡 Suggestions:")
        for r in results:
            st.markdown(f"- {r}")
    else:
        st.success("✅ No confusing jargon detected!")
