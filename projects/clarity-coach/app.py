import streamlit as st
from coach import analyze_text

st.set_page_config(page_title="🧠 Clarity Coach", layout="centered")

st.title("🧠 Clarity Coach")
st.write("Paste your technical writing below. This tool will find jargon, explain it, and offer simpler rewrites.")

text = st.text_area("📄 Input Text", height=200)

if st.button("🔍 Analyze"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        results = analyze_text(text)

        if results:
            st.markdown("### ✨ Results")
            for item in results:
                st.markdown(f"""
                - **Term**: `{item['term']}`  
                  - 📖 *Meaning*: {item['meaning']}  
                  - 🔁 *Simpler Alternative*: `{item['simpler']}`  
                  - ✏️ *Suggested Rewrite*:  
                    `{item['rewrite']}`
                """)
        else:
            st.success("✅ No jargon detected. Great job!")
