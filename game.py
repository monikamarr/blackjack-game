## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import sys

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}


dealer_deck = []
player_deck = []
player_deck_to_print = []
dealer_deck_to_print = []



next_round = input("Would you like to play Blackjack? y/n  ")

if next_round == "n":
    print("Ok bye!")
    sys.exit()

# player's first card
player_card_tuple = random.choice(list(cards.items()))
k, v = player_card_tuple
player_deck.append(v)
player_deck_to_print.append(k)


# dealer's first two cards
for i in range(2):
    dealer_card_tuple = random.choice(list(cards.items()))
    key, value = dealer_card_tuple
    dealer_deck.append(value)
    dealer_deck_to_print.append(key)
sum_of_dealer = sum(dealer_deck)
# print(f"sum of house: {sum_of_dealer}")
print(f"Dealer's cards: [{dealer_deck_to_print[0]}, ♤]")



while next_round.lower() == "y":

    # for the player
    sum_of_player = 0
    player_card_tuple = random.choice(list(cards.items()))
    k, v = player_card_tuple
    player_deck.append(v)
    player_deck_to_print.append(k)

    for i in player_deck:
        if sum_of_player <= 10:
            cards["A"] = 11
        elif sum_of_player > 10:
            cards["A"] = 1
        sum_of_player += i

    print(f"Your cards: {player_deck_to_print}")
    print(f"Sum of your cards: {sum_of_player}")

    if sum_of_player == 21:
        break

    if sum_of_player > 21:
        print("You lose!!!!")
        break

    next_round = input("Do you want to draw another card? y/n")

    if sum_of_player < 15 and next_round == "n":
        print("You did illegal exit. You lose!!!")

    # print(f"here dealers before taking dealer's way: {sum_of_dealer}")

    if next_round == "n":

        # for the dealer
        while sum_of_dealer + 1 < sum_of_player and sum_of_dealer <= 21:
            print(f"dealer's deck: {dealer_deck}")
            sum_of_dealer = 0
            for i in dealer_deck:
                if sum_of_dealer <= 10:
                    cards["A"] = 11
                elif sum_of_dealer > 10:
                    cards["A"] = 1
                sum_of_dealer += i
            # print(f"here after calc sum: {sum_of_dealer}")



            if sum_of_dealer < sum_of_player:

                dealer_card_tuple = random.choice(list(cards.items()))
                key, value = dealer_card_tuple
                dealer_deck.append(value)
                dealer_deck_to_print.append(key)
                # print(f"last dealer's: {dealer_deck_to_print}")
            elif sum_of_dealer >= sum_of_player:
                break

print(f"Cards of the house: {dealer_deck_to_print}")
print(f"Sum of the house: {sum_of_dealer}")


if sum_of_player == sum_of_dealer:
    print("DRAW!")

elif sum_of_player > sum_of_dealer and 15 < sum_of_player <= 21:
    print("You win!!!")

elif sum_of_player < sum_of_dealer <= 21:
    print("House wins!!")

else:
    print("House wins!")