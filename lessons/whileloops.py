"""Demonstrate while loops by finding low value of string"""

cards: str = "5235"
card_inx: int = 0
low_card: int = int(cards[0])

while card_inx < 4:
    current_card: int = int(cards[card_inx])
    if (current_card < low_card):
        low_card = current_card
    card_inx += 1
print(low_card)