# 🧩 Code Formatter

A lightweight Python utility that automatically reformats Python source code using the built-in **Abstract Syntax Tree (AST)** module.  
It reads your code, parses it for structure, and regenerates a clean, consistently formatted version — perfect for improving readability and ensuring syntax integrity.

---

## 🚀 Features

- Parses Python code into an **AST (Abstract Syntax Tree)** and regenerates it cleanly  
- Re-formats inconsistent or messy Python code instantly  
- Provides clear, readable output directly in the terminal  
- Includes graceful error handling for invalid syntax or missing files  
- Designed for quick developer productivity and script cleanup

---

## 🧠 How It Works

1. The script reads a Python file you specify  
2. It parses the file into an **AST representation** of the code  
3. The AST is converted (unparsed) back into clean, properly spaced code  
4. The formatted code is printed to your terminal, ready for use

---

## ⚙️ Usage

## Command Line
```bash
python formatter.py <file-to-format.py>

```
## 🧩 Example - You can test the script with a sample file named sample_script.py:

**Input**
x=1
print(x +2)

**Output**
x = 1
print(x + 2)


```
python formatter.py sample_script.py
```

---

## 📄 **License**


This project is licensed under the MIT License — feel free to modify and use it for your own projects.

✅ This is **one unified block** — no fragments, no scrolling back and forth, no missing code fences.  
It will render perfectly in GitHub’s dark mode just like your screenshots, clean and structured.
