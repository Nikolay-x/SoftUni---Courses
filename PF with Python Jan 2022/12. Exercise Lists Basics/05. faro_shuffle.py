# 5.Faro Shuffle
# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.
#
# Input
# a b c d e f g h
# 5
#
# Output
# ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']

cards_deck = input().split(" ")
shuffles_count = int(input())

# for i in range(shuffles_count):
#
#     deck1 = cards_deck[:len(cards_deck) // 2]
#     deck2 = cards_deck[len(cards_deck) // 2:]
#
#     cards_deck = [c for pair in zip(deck1, deck2) for c in pair]
#
# print(cards_deck)

for i in range(shuffles_count):

    deck1 = cards_deck[:len(cards_deck) // 2]
    deck2 = cards_deck[len(cards_deck) // 2:]

    cards_deck = []

    for pair in zip(deck1, deck2):
        cards_deck += pair

print(cards_deck)
