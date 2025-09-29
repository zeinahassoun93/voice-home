import spacy
from spacy.matcher import Matcher

# nlp = spacy.load("en_core_web_sm")
nlp = spacy.blank("en")

matcher = Matcher(nlp.vocab)

# Basic patterns

patterns = {
    "LIGHT_ON":[
            [{"LOWER": "turn"}, {"LOWER": "on"}, {"LOWER": "light"}],
            [{"LOWER": "switch"}, {"LOWER": "on"}, {"LOWER": "light"}],
            [{"LOWER": "light"}, {"LOWER": "on"}],
            [{"LOWER": "on"}, {"LOWER": "light"}]
        ],
    "LIGHT_OFF":[ 
            [{"LOWER": "turn"}, {"LOWER": "off"}, {"LOWER": "light"}],
            [{"LOWER": "switch"}, {"LOWER": "off"}, {"LOWER": "light"}],
            [{"LOWER": "light"}, {"LOWER": "off"}],
            [{"LOWER": "off"}, {"LOWER": "light"}]

            ],
    "FAN_ON": [
        [{"LOWER": "turn"}, {"LOWER": "on"}, {"LOWER": "fan"}],
        [{"LOWER": "fan"}, {"LOWER": "on"}],
        [{"LOWER": "on"}, {"LOWER": "fan"}]
    ],
    "FAN_OFF": [
        [{"LOWER": "turn"}, {"LOWER": "off"}, {"LOWER": "fan"}],
        [{"LOWER": "fan"}, {"LOWER": "off"}],
        [{"LOWER": "off"}, {"LOWER": "fan"}],

    ]        
}
for intent, pattern in patterns.items():
    matcher.add(intent, pattern)

def get_intent(text):
    doc = nlp(text)
    matches = matcher(doc)
    if matches:
        match_id, start, end = matches[0]
        intent = nlp.vocab.strings[match_id]
        return intent
    else:
        return "UNKNOWN" 
