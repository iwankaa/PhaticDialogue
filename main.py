import random
from adjective import *
from get_nouns import *
from get_verbs import *
from imports import greet, dummy_phrases

def get_ans():
    ans = input("> ")
    return ans

def run():
    print(random.choice(greet))
    while True:
        inp = get_ans()
        if inp.lower() == "bye":
            print("Nice talking to you! Bye!")
            return
        nouns = get_nouns(inp)
        verb_lemmas = get_verb_lemmas(inp)
        adjective = get_adj_sentiments(inp)
        response_candidates = []
        if nouns:
            response_candidates.extend(reflect_noun(noun) for noun in nouns)
        if verb_lemmas:
            response_candidates.extend(hamlet(vl) for vl in verb_lemmas)
        if adjective:
            response_candidates.extend(reflect_adj(adj['text'], adj['sent']) for adj in adjs_sents)
        if not response_candidates:
            response_candidates.extend(dummy_phrases)
        random.shuffle(response_candidates)
        print(random.choice(response_candidates))

if __name__ == "__main__":
    run()
