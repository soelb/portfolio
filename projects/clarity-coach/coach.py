import spacy
from fuzzywuzzy import process

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

# Example dictionary of valid words (expand this for better coverage)
VALID_WORDS = [
    "organize", "projects", "which", "should", "doing", "once", "first", "feel",
    "asynchronous", "microservices", "orchestration", "distributed", "tracing"
]

def correct_spelling(text):
    corrected_words = []
    for word in text.split():
        if word.lower() in VALID_WORDS:
            corrected_words.append(word)
        else:
            match, score = process.extractOne(word, VALID_WORDS)
            if score > 80:  # threshold for confidence
                corrected_words.append(match)
            else:
                corrected_words.append(word)
    return " ".join(corrected_words)

def analyze_text(text):
    # Step 1: Correct spelling
    corrected_text = correct_spelling(text)

    # Step 2: Grammar cleanup using spaCy
    doc = nlp(corrected_text)
    clean_sentences = []
    for sent in doc.sents:
        tokens = [token.text for token in sent]
        clean_sentences.append(" ".join(tokens).replace(" ,", ",").replace(" .", "."))
    grammar_fixed_text = " ".join(clean_sentences)

    # Step 3: Replace jargon with simpler alternatives
    final_text = grammar_fixed_text
    jargon_hits = []
    for jargon_term, explanation in JARGON_DB.items():
        if jargon_term in final_text.lower():
            jargon_hits.append({
                "term": jargon_term,
                "meaning": explanation["meaning"],
                "simpler": explanation["simpler"]
            })
            final_text = final_text.replace(jargon_term, explanation["simpler"])

    return {
        "original": text,
        "corrected_spelling": corrected_text,
        "grammar_fixed": grammar_fixed_text,
        "final_rewrite": final_text,
        "jargon_replacements": jargon_hits
    }

# Optional test
if __name__ == "__main__":
    sample = "i ned to orgnize my proejcts but idk wich shud go first an we utilize asynchronous microservices with robust orchestration."
    output = analyze_text(sample)

    print("Original:", output["original"])
    print("Corrected spelling:", output["corrected_spelling"])
    print("Grammar fixed:", output["grammar_fixed"])
    print("Final rewrite:", output["final_rewrite"])
    if output["jargon_replacements"]:
        print("\nJargon replacements made:")
        for item in output["jargon_replacements"]:
            print(f"{item['term']} → {item['simpler']} ({item['meaning']})")
