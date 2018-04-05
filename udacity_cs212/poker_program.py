#!/usr/bin/env python2

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)


def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks)) # 2 3 4 5 6 (8, 6)
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks)) # 9 9 9 9

    return None


def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() #sf straight flush
    fk = "9D 9H 9S 9C 7D".split() #fk four of the kind
    fh = "TD TC TH 7C 7D".split() #fh full house
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([fh]) == fh
    assert poker([sf] + 99*[fh]) == sfn
    return "tests pass"


print test()