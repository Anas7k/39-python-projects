from replit import clear
#HINT: You can call clear() to clear the output in the console.only if you are using replit other wise make it as comment it will be error
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
    highest_bidder = 0
    winner =""
    for i in bids:
      bid_amount= bids[i]
  
      if bid_amount > highest_bidder:
        highest_bidder = bid_amount
        winner = i
    print(f"The winner is {winner} with a bid of ${highest_bidder}")

