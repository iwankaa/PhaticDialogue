import random

from textblob import TextBlob

from imports import nlp


def get_adj_sentiments(article):
    doc = nlp(article)

    adjs_sents = []

    for token in doc:

        if token.pos_ == "ADJ":
            adjs_sents.append({'text': token.text, 'sent': TextBlob(token.text).sentiment.polarity})

    return adjs_sents


def reflect_adj(adj, sent):
    mirror_phrases = ["It seems that you feel ", "It looks like you feel ", "It appears like you feel "]

    if sent <= -0.5:

        return random.choice(mirror_phrases) + "embarrased"

    elif sent > -0.5 and sent <= 0:

        return random.choice(mirror_phrases) + "not ok"

    elif sent > 0 and sent <= 0.5:

        return random.choice(mirror_phrases) + "fine"

    elif sent > 0.5:

        return random.choice(mirror_phrases) + "awesome"
