
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

=======
# portfolio
A central hub for my projects, tools, and developer journey
<h1 align="center">Hey there 👋 I'm Soeleece Benjamin</h1>
<p align="center">
  I buildd tools that make workflows simpler, faster, and more empowering. 
</p>

---

## 🗣️ About Me

- I don't define myself as a developer - I build things that matter.
- Currently building a platform for engineers, analysts, project managers & more.
- Passionate about becoming a **start-to-finish engineer** - from backend to frontend and everything in between.
- Exploring tools that connect technical silos and bring ideas to life, end-to-end.

---

## 🛠️ Tech Stack & Tools 

| Platform | Tools |
| ---------|-------|
| Backend | Python, Supabase |
| Frontend | Vercel, Markdown, Terminal UI |

---

## 📝 Projects

### ⏳ Command Time Travel
> Explore your shell history like a time traveler – last week, last month, or this day last year.

🔗 [View Gist](./projects/command-time-travel/README.md)

### 📊 Engineer's Dashboard
> A terminal-based dashboard that gives engineers a quick overview of system status and active tasks.

🔗 [View Code](./projects/engineers-dashboard)

### 🧹 Code Formatter  
> A simple tool that takes in messy Python code and returns a clean, formatted version using AST.

🔗 [View Code](./projects/code-formatter)

### 🕵🏽‍♀️ Jargon Detector 
> This tool analyzes technical writing and highlights complex, buzzword-heavy jargon. It’s designed to make documentation clearer and more accessible — perfect for onboarding, technical handoffs, and user education.

> Using Natural Language Processing (NLP) via [spaCy](https://spacy.io), the detector identifies advanced terminology and recommends simpler alternatives.

[View Code](./projects/jargon-detector)

<!-- Add more projects below -->

---

## 📫 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn--blue?logo=linkedin&style=social)](https://www.linkedin.com/in/https://www.linkedin.com/in/soeleece-benjamin-821532231/)

