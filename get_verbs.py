from imports import nlp


def get_verb_lemmas(article):

  doc = nlp(article)

  verb_lemmas = []

  for token in doc:

    if token.pos_ == "AUX" or token.pos_ == "VERB":

      verb_lemmas.append(token.lemma_)

  return verb_lemmas




def hamlet(verb):

  return "To " + verb + ", or not to " + verb + ", that is the question"