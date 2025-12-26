import spacy
from typing import List

# Enable GPU if available
try:
    spacy.require_gpu()
except Exception:
    pass

nlp = spacy.load("en_core_web_trf")

def extract_entities(text: str):
    doc = nlp(text)
    return [
        {
            "text": ent.text,
            "label": ent.label_,
            "start": ent.start_char,
            "end": ent.end_char,
        }
        for ent in doc.ents
    ]

def extract_entities_batch(texts: List[str], batch_size: int = 8):
    results = []
    for doc in nlp.pipe(texts, batch_size=batch_size):
        results.append([
            {
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char,
            }
            for ent in doc.ents
        ])
    return results

