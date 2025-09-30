import spacy
from fuzzywuzzy import process
from wordfreq import top_n_list

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Build a large dictionary of English words from wordfreq (top 50,000 words)
VALID_WORDS = set(top_n_list("en", 50000))

# Define your jargon dictionary
JARGON_DB = {
    "asynchronous": {"simpler": "non-blocking"},
    "microservices": {"simpler": "small services"},
    "orchestration": {"simpler": "coordination"},
    "distributed tracing": {"simpler": "system tracking"},
}

def correct_spelling(text):
    corrected_words = []
    for word in text.split():
        word_lower = word.lower()
        if word_lower in VALID_WORDS:
            corrected_words.append(word)
        else:
            match, score = process.extractOne(word_lower, VALID_WORDS)
            if score and score > 85:
                corrected_words.append(match)
            else:
                corrected_words.append(word)
    return " ".join(corrected_words)

def analyze_text(text):
    # Step 1: Correct spelling
    corrected_text = correct_spelling(text)

    # Step 2: Grammar cleanup
    doc = nlp(corrected_text)
    clean_sentences = []
    for sent in doc.sents:
        tokens = [token.text for token in sent]
        clean_sentences.append(" ".join(tokens).replace(" ,", ",").replace(" .", "."))
    grammar_fixed_text = " ".join(clean_sentences)

    # Step 3: Replace jargon
    final_text = grammar_fixed_text
    for jargon_term, explanation in JARGON_DB.items():
        if jargon_term in final_text.lower():
            final_text = final_text.replace(jargon_term, explanation["simpler"])

    return final_text

# Optional test
if __name__ == "__main__":
    sample = "i ned to orgnize my proejcts but idk wich shud go first an we utilize asynchronous microservices with robust orchestration."
    polished = analyze_text(sample)
    print("Final polished rewrite:", polished)
