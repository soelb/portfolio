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

            st.markdown("**📝 Original Text:**")
            st.info(results["original"])

            st.markdown("**✅ Polished Version:**")
            st.success(results["polished"])

            st.markdown("**🔧 Changes Made:**")
            for i, change in enumerate(results["changes"]):
                cat = results["categories"][i] if i < len(results["categories"]) else "unspecified"
                st.markdown(f"- [{cat}] {change}")

            st.markdown("**📊 Stats:**")
            stats = results["stats"]
            st.json(stats)
        else:
            st.success("✅ No jargon detected. Great job!")
