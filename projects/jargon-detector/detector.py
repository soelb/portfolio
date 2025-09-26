import spacy

# Load English tokenizer, POS tagger, etc.
nlp = spacy.load("en_core_web_sm")

# Define a list of known "jargon" terms (can expand later or use embeddings)
JARGON = {
    "orchestration": "coordination",
    "microservices": "small services",
    "containerized": "packaged",
    "distributed tracing": "tracking across systems",
    "observability": "monitoring",
    "asynchronous": "non-blocking",
    "auto-scaling": "automatic scaling"
}

def detect_jargon(text):
    doc = nlp(text)
    found = []

    for token in doc:
        lower = token.text.lower()
        if lower in JARGON:
            found.append((token.text, JARGON[lower]))
    
    return found

# Read the file
with open("projects/jargon-detector/sample.txt", "r") as file:
    content = file.read()

jargon_terms = detect_jargon(content)

if jargon_terms:
    print("\n🧪 Jargon detected:")
    for original, suggestion in jargon_terms:
        print(f" - {original} → try: '{suggestion}'")
else:
    print("✅ No jargon detected!")

