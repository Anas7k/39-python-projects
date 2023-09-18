from replit import clear
#HINT: You can call clear() to clear the output in the console.only if you are using replit other wise make comment
from art import logo
print(logo)
print("Welcome to the secret auction program.")
end = True

bids ={}

while end:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bids[name] = bid    

  another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
  if another_bidder == "yes":
    clear()
    end = True
  else:
    end = False
    bid_amount= ()
    highest_bidder = 0
    # win =""
    for i in bids:
      bid_amount= bids[i]
  
      if bid_amount > highest_bidder:
        highest_bidder = bid_amount
        # win = i
    print(f"The winner is {name} with a bid of ${highest_bidder}")
