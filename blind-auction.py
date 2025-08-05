from art import logo

print(logo)

bid_dict = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = input("What is your bid? $")
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")

    bid_dict[name] = price
    print("\n" * 20)

    if other_bidders.lower() == 'no':
        continue_bidding = False

highest_price = max(bid_dict.values())
name_highest_price = max(bid_dict, key=bid_dict.get)

print(f"The winner is {name_highest_price} with a bid of ${highest_price}")
