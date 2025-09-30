import spacy

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


def analyze_text(text):
    doc = nlp(text)
    results = []

    for chunk in doc.noun_chunks:
        phrase = chunk.text.lower()

        if phrase in JARGON_DB:
            explanation = JARGON_DB[phrase]
            results.append({
                "term": chunk.text,
                "meaning": explanation["meaning"],
                "simpler": explanation["simpler"],
                "rewrite": text.replace(chunk.text, explanation["simpler"])
            })

    return results


# Test it from CLI (optional)
if __name__ == "__main__":
    sample = "We use asynchronous microservices and leverage orchestration for distributed tracing."
    output = analyze_text(sample)

    for item in output:
        print(f"{item['term']} → {item['simpler']} ({item['meaning']})")
