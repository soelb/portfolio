import spacy

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Dictionary of known jargon terms mapped to simpler alternatives
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
    """
    Detects jargon terms in the given text and suggests simpler alternatives.

    Args:
        text (str): The input text to analyze.

    Returns:
        list of tuples: Each tuple contains the original term and its simpler alternative.
    """
    doc = nlp(text)
    found = []

    for token in doc:
        lower = token.text.lower()
        if lower in JARGON:
            found.append((token.text, JARGON[lower]))
    
    return found

# Read content from the sample file
with open("projects/jargon-detector/sample.txt", "r") as file:
    content = file.read()

# Run the jargon detector
jargon_terms = detect_jargon(content)

# Display results
if jargon_terms:
    print("\n🧪 Jargon detected:")
    for original, suggestion in jargon_terms:
        print(f" - {original} → try: '{suggestion}'")
else:
    print("✅ No jargon detected!")
