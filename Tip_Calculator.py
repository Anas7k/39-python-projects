#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator.")
total_bill = (input("What was the total bill? $"))
percentage_of_tip = (input("What percentage tip would you like to give 10, 12 or 15? "))
people_to_split = (input("How many people to spilt the bill? "))
total_percentage_of_tip = int(percentage_of_tip) / 100 * float(total_bill)
total_with_tip = float(total_bill) + total_percentage_of_tip
amount_per_person =  total_with_tip / int(people_to_split)
print("Each person should pay: $", "{:.2f}" .format(amount_per_person))
