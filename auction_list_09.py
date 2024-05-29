
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
auction = []

def add_bidder(name, bid):
    bidder = {}
    bidder["name"] = name
    bidder["bid"]= float(bid)
    auction.append(bidder)
    
flag = True

while flag:
    name = input("Enter your Name ")
    bid = input("Enter your Bid $")
    add_bidder(name,bid)
    
    ask = input("Is there any other bidder?").lower()
    
    if ask == "no":
        flag = False
        
highest_bidder=""
highest_bid =0

for bidder in auction:
    if bidder["bid"] > highest_bid:
        highest_bidder = bidder["name"]
        highest_bid = bidder["bid"]
        
print(f"The highest bidder is {highest_bidder} with highest bid of ${highest_bid}!")        