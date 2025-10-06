import streamlit as st
from coach import analyze_text

st.set_page_config(page_title="🧠 Clarity Coach", layout="centered")

st.title("🧠 Clarity Coach")
st.write("Paste your technical writing below. This tool will find jargon, grammar, and clarity issues — then offer a cleaner rewrite.")

text = st.text_area("📄 Input Text", height=200)

if st.button("🔍 Analyze"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        results = analyze_text(text)

        # Display main results
        st.markdown("### ✨ Results")
        st.markdown("**📝 Original Text:**")
        st.info(results["original"])

        st.markdown("**✅ Polished Version:**")
        st.success(results["polished"])

        # Display detailed change list
        st.markdown("**🔧 Changes Made:**")
        if results["changes"]:
            for i, change in enumerate(results["changes"]):
                cat = results["categories"][i] if i < len(results["categories"]) else "unspecified"
                st.markdown(f"- **[{cat}]** {change}")
        else:
            st.markdown("No changes were needed!")

        # Display stats
        st.markdown("**📊 Stats:**")
        st.json(results["stats"])
