#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import difflib
from datetime import datetime
import spacy
from fuzzywuzzy import process
from wordfreq import top_n_list

# -------------------------------------------------
# Core settings
# -------------------------------------------------
NLP_MODEL = "en_core_web_sm"
FUZZY_SCORE = 92
VALID_WORDS = set(top_n_list("en", 50000))

# Whitelist to *never* auto-correct
TECH_WHITELIST = {
    "cross-functional", "holistically", "microservices", "containerized",
    "orchestration", "observability", "devops", "cloud-native", "end-user",
    "latency", "interoperability", "scalability", "refactor", "pipeline",
}

JARGON_DB = {
    "asynchronous": {"simpler": "non-blocking", "category": "jargon"},
    "microservices": {"simpler": "small services", "category": "jargon"},
    "orchestration": {"simpler": "coordination", "category": "jargon"},
    "distributed tracing": {"simpler": "system tracking", "category": "jargon"},
    "observability": {"simpler": "monitoring", "category": "jargon"},
}

SLANG_MAP = {
    "gonna": "going to", "wanna": "want to", "cuz": "because",
    "tho": "though", "idk": "I don't know", "btw": "by the way",
    "imo": "in my opinion", "u": "you", "ur": "your", "pls": "please",
}

CONTRACTIONS = {
    "dont": "don't", "cant": "can't", "wont": "won't", "shouldnt": "shouldn't",
    "wouldnt": "wouldn't", "couldnt": "couldn't", "isnt": "isn't",
    "wasnt": "wasn't", "arent": "aren't", "werent": "weren't",
    "havent": "haven't", "hasnt": "hasn't", "hadnt": "hadn't",
    "doesnt": "doesn't", "didnt": "didn't", "aint": "ain't",
}

import re

GRAMMAR_FIXES = {
    r"\bain['’]t\b": "is not",
    r"\bAin['’]t\b": "is not",
    # (then keep the rest of your patterns)
    r"\ban we\b": "and we",
    r"\ban i\b": "and I",
    r"\bgonna\b": "going to",
    r"\bwanna\b": "want to",
    r"\bcuz\b": "because",
    r"\bcould of\b": "could have",
    r"\bshould of\b": "should have",
    r"\bwould of\b": "would have",
    r"\balot\b": "a lot",
    r"\birregardless\b": "regardless",
    r"\beachother\b": "each other",
    r"\beveryother\b": "every other",
    r"\bdue to the fact that\b": "because",
    r"\bin order to\b": "to",
    r"\bat this point in time\b": "now",
    r"\bfor all intensive purposes\b": "for all intents and purposes"
}

def apply_simple_fixes(text: str):
    changes, cats = [], []
    for pattern, repl in GRAMMAR_FIXES.items():
        def _sub(m):
            changes.append(f"{m.group(0)} → {repl}")
            cats.append("grammar")
            return repl
        text = re.sub(pattern, _sub, text, flags=re.IGNORECASE)
    return text, changes, cats


CODE_LIKE_CHARS = set("{}[]()<>;:/\\'\"$#@_|~`^")

nlp = spacy.load("en_core_web_sm")


def looks_like_code_token(tok: str) -> bool:
    return any(c in CODE_LIKE_CHARS for c in tok) or "_" in tok or any(c.isdigit() for c in tok)

def looks_like_domain_term(tok: str) -> bool:
    return "-" in tok or "." in tok or any(c.isupper() for c in tok if c.isalpha()) or len(tok) > 12

# -------------------------------------------------
# Fix passes
# -------------------------------------------------
def correct_spelling(text: str):
    changes, cats, out = [], [], []

    for word in text.split():
        w = word.lower()

        if w in SLANG_MAP:
            out.append(SLANG_MAP[w])
            changes.append(f"{word} → {SLANG_MAP[w]}")
            cats.append("slang")
            continue

        if w in CONTRACTIONS:
            out.append(CONTRACTIONS[w])
            changes.append(f"{word} → {CONTRACTIONS[w]}")
            cats.append("contraction")
            continue

        if (
            w in VALID_WORDS
            or word in TECH_WHITELIST
            or looks_like_code_token(word)
            or looks_like_domain_term(word)
        ):
            out.append(word)
            continue

        match, score = process.extractOne(w, VALID_WORDS)
        if score and score >= FUZZY_SCORE and len(word) > 2:
            out.append(match)
            changes.append(f"{word} → {match}")
            cats.append("spelling")
        else:
            out.append(word)

    return " ".join(out), changes, cats


def sentence_cleanup(text: str):
    doc = nlp(text)
    sents = []
    for sent in doc.sents:
        s = " ".join([t.text for t in sent])
        s = s.replace(" ,", ",").replace(" .", ".").strip()
        if s:
            s = s[0].upper() + s[1:]
        sents.append(s)
    return " ".join(sents)


def smooth_grammar(text: str):
    fixed = f" {text} "
    changes, cats = [], []
    for bad, good in GRAMMAR_FIXES.items():
        if bad in fixed:
            fixed = fixed.replace(bad, good)
            changes.append(f"{bad.strip()} → {good.strip()}")
            cats.append("grammar")
    return fixed.strip(), changes, cats


def replace_jargon(text: str):
    changes, cats = [], []
    final = text
    for term, meta in sorted(JARGON_DB.items(), key=lambda kv: -len(kv[0])):
        if term in final.lower():
            final = final.replace(term, meta["simpler"])
            changes.append(f"{term} → {meta['simpler']}")
            cats.append(meta["category"])
    return final, changes, cats


def compute_simple_pairs(a: str, b: str):
    sm = difflib.SequenceMatcher(None, a.split(), b.split())
    return [(" ".join(a.split()[i1:i2]), " ".join(b.split()[j1:j2])) for _, i1, i2, j1, j2 in sm.get_opcodes()]


# -------------------------------------------------
# Public API
# -------------------------------------------------
def analyze_text(text: str):
    # Step 1: Apply grammar and slang fixes *first*
    step0, ch0, cat0 = apply_simple_fixes(text)

    # Step 2: Then spelling and contractions
    step1, ch1, cat1 = correct_spelling(step0)

    # Step 3: Sentence cleanup
    step2 = sentence_cleanup(step1)

    # Step 4: Replace jargon
    final, ch3, cat3 = replace_jargon(step2)

    # Merge all change logs
    changes = ch0 + ch1 + ch3
    cats = cat0 + cat1 + cat3

    # Stats
    stats = {
        "words_before": len(text.split()),
        "words_after": len(final.split()),
        "num_changes": len(changes),
        "by_category": {
            "spelling": cats.count("spelling"),
            "slang": cats.count("slang"),
            "contraction": cats.count("contraction"),
            "grammar": cats.count("grammar"),
            "jargon": cats.count("jargon"),
        },
    }

    # Cleanup small cosmetic spacing issues
    final = (
        final.replace(" - ", "-")
             .replace(" ,", ",")
             .replace(" .", ".")
             .replace(" ’", "’")
             .replace(" n't", "n't")
    )

    return {
        "original": text,
        "polished": final,
        "changes": changes,
        "categories": cats,
        "stats": stats,
        "diff_pairs": compute_simple_pairs(text, final),
    }
