 # 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza of do you want? S, M, or L: ").lower()
print(size)
add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
print(add_pepperoni)
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
print(extra_cheese)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")

  




