# coach.py

"""
Clarity Coach:
Explains why certain technical terms may be confusing and provides simpler alternatives.
"""

JARGON_EXPLAINER = {
    "orchestration": {
        "explanation": "Often sounds like a buzzword — just means coordinating tasks or services.",
        "replacement": "coordination"
    },
    "asynchronous": {
        "explanation": "Many people don’t understand async — it just means things happen without waiting in line.",
        "replacement": "non-blocking"
    },
    "observability": {
        "explanation": "It's a fancy way to say 'seeing what's going on inside a system.'",
        "replacement": "monitoring"
    },
    "containerized": {
        "explanation": "Technical term from DevOps — just means packaged into a portable format.",
        "replacement": "packaged"
    }
}

def explain_term(term):
    lower = term.lower()
    return JARGON_EXPLAINER.get(lower, None)

