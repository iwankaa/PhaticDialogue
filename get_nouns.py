import random

from imports import nlp


def get_nouns(article):
    doc = nlp(article)
    nouns = []
    for token in doc:
        if token.pos_ == "PROPN" or token.pos_ == "NOUN":
            nouns.append(token.text)
    return nouns


def reflect_noun(noun):
    mirror_phrases = ["... Interesting...", "? Hmm... ", "? Really?", "? Doesn't sound right...", ]
    return noun.title() + random.choice(mirror_phrases)
