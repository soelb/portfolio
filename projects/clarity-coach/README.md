# 🧠 Clarity Coach — Your Jargon-Busting Writing Assistant

Clarity Coach is an upgraded version of [Jargon Detector](../jargon-detector), designed to do more than just flag confusing terms.

It *explains* them. And suggests *better* alternatives.

## ✨ What It Does

Paste in a chunk of technical writing (e.g., from a README or doc), and Clarity Coach will:

✅ Detect jargon  
✅ Explain what it means  
✅ Suggest simpler alternatives  
✅ Offer a rewrite in plain English

---

### 💡 Example

**Input:**

> "We use asynchronous microservices and leverage orchestration for distributed tracing."

**Output:**

| Term              | Meaning                      | Simpler Term      | Suggested Rewrite                             |
|-------------------|------------------------------|-------------------|-----------------------------------------------|
| asynchronous      | Not happening at same time   | non-blocking      | "We use non-blocking services..."             |
| microservices     | Small independent components  | small services    | "...built from small services"                |
| orchestration     | Coordinated management       | coordination      | "...with coordination for tracking"           |
| distributed tracing | Tracking across systems    | system tracking   | "...and system tracking tools"                |

---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [spaCy](https://spacy.io/) or `transformers` (for NLP)
- [Streamlit](https://streamlit.io/) (for interactive UI)
- JSON file (for jargon-to-plain-English mappings)

---

## 🚀 How to Run It (Locally or in Codespaces)

**In GitHub Codespaces:**

> 1. Open this repo in Codespaces  
> 2. Open `projects/clarity-coach/app.py`  
> 3. Press `Run` ▶️ or run:  
>    ```
>    streamlit run app.py
>    ```

---

## 📌 Roadmap

- [ ] Build the core logic in `coach.py`
- [ ] Add Streamlit UI in `app.py`
- [ ] Improve rewrite suggestions
- [ ] Handle more domains (e.g. legal, marketing)

---

## 🧠 Why This Project?

Because communication is as important as code.

Clarity Coach helps technical teams write docs that are inclusive, clear, and actually helpful — especially for new devs, cross-functional partners, and open-source users.

---

⚠️ Security Note

Real credentials (like API keys or OAuth secrets) should never be committed to the repository.
For development, use the included credentials_template.json file and replace its placeholder values locally.
The .gitignore file ensures that your private credentials.json stays protected and out of version control.

