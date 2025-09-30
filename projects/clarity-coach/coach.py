import spacy
from fuzzywuzzy import fuzz

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Define your jargon dictionary
JARGON_DB = {
    "asynchronous": {
        "meaning": "Not happening at the same time",
        "simpler": "non-blocking",
    },
    "microservices": {
        "meaning": "Small, independent components that work together",
        "simpler": "small services",
    },
    "orchestration": {
        "meaning": "Coordinated management of services or tasks",
        "simpler": "coordination",
    },
    "distributed tracing": {
        "meaning": "Tracking events across systems or services",
        "simpler": "system tracking",
    }
}

def find_closest_jargon(term):
    for jargon_term in JARGON_DB:
        ratio = fuzz.ratio(term.lower(), jargon_term.lower())
        if ratio >= 85:  # You can adjust this threshold
            return jargon_term
    return None

def analyze_text(text):
    doc = nlp(text)
    results = []

    for chunk in doc.noun_chunks:
        phrase = chunk.text.lower()
        match = None

        if phrase in JARGON_DB:
            match = phrase
        else:
            match = find_closest_jargon(phrase)

        if match:
            explanation = JARGON_DB[match]
            results.append({
                "term": chunk.text,
                "meaning": explanation["meaning"],
                "simpler": explanation["simpler"],
                "rewrite": text.replace(chunk.text, explanation["simpler"])
            })

    return results

# Optional test
if __name__ == "__main__":
    sample = "Our platform utilizes asynchronous microservices with robust orchestration and distributed tracing to ensure scalability."
    output = analyze_text(sample)

    for item in output:
        print(f"{item['term']} → {item['simpler']} ({item['meaning']})")
