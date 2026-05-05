from art import logo

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(logo)
blind_auction = {}
wants_to_bid = True
max_bid = -1
top_bidder =""
highest_bid = 0

while wants_to_bid:
    bidder_name = input("what is your name?:")
    bid_price = int(input("bid price:"))

    blind_auction[bidder_name] = bid_price

    contniue =input(f"there are other users who want to bid? type 'yes' if wants to continue,"
                            f"Otherwise, type 'no' if wants to stop bidding. ").lower()
    if contniue == "no":
        wants_to_bid = False
    elif contniue == "yes":
        wants_to_bid = True
    else:
        print("Inavlid response, Kindly give the valid response.")
        contniue = input(f"there are other users who want to bid? type 'yes' if wants to continue,"
                         f"Otherwise, type 'no' if wants to stop bidding. ").lower()
# print("\n" * 50)

print(blind_auction)

# we can use max function to get the highest bid
# top_bidder = max(blind_auction, key=blind_auction.get)
# highest_bid = blind_auction[top_bidder]
# print(top_bidder,highest_bid)

for bidder in blind_auction:
    if blind_auction[bidder] > max_bid:
        max_bid = blind_auction[bidder]
        top_bidder = bidder

print(top_bidder,max_bid)

