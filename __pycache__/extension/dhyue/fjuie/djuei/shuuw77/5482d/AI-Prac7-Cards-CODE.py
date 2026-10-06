import random

# Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jack', 'Queen', 'King', 'Ace']

deck = []

# Generate 52 cards
for suit in suits:
    for rank in ranks:
        deck.append(rank + ' of ' + suit)

# Display original deck
print("Original Deck:")
for card in deck:
    print(card)

# Shuffle the deck
random.shuffle(deck)

# Display shuffled deck
print("\nShuffled Deck:")
for card in deck:
    print(card)
