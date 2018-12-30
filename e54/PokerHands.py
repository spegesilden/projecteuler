hands = {'High Card': 0,
        'One Pair': 1,
        'Two Pairs': 2,
        'Three of a Kind': 3,
        'Straight': 4,
        'Flush': 5,
        'Full house': 6,
        'Four of a king': 7,
        'Straight Flush': 8,
        'Royal Straight Flush': 9}

cards = {'2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14}

def highCard(hand):
    h = 0

    for card in hand:
        c = cards[card[0]]
        h = max(c, h)

    return str(h)

