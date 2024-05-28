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
auction = {}

def add_bidder(name, bid):
    auction[name] = float(bid)
    
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
    if auction[bidder] > highest_bid:
        highest_bidder = bidder
        highest_bid = auction[bidder]
        
print(f"The highest bidder is {highest_bidder} with highest bid of ${highest_bid}!")        