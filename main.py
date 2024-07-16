from menu import MENU, resources
import os

# fuction to check the resources are enough or not   
def check_resources(coffee):
  for i in MENU[coffee]["ingredients"]:
      for r in resources:
          if r == i:
              if MENU[coffee]["ingredients"][i] > resources[r]:
                  return r
              else:
                  pass
                    
                  
# function coins to count and ask the user coins
def coins():
    quarter = int(input("\nhow many quarters? "))
    dime = int(input("\nhow many dimes? "))
    nickle = int(input("\nhow many nickles? "))
    penny = int(input("\nhow many pennies? "))

    q = quarter / 4
    d = dime / 10
    n = nickle / 20
    p = penny / 100

    add = q + d + n + p
    return add

# function to check the cost of the coffee
def check_cost(coffee):
  if MENU[coffee]["cost"] > payment:
      money = "\nnot enough payment"
      return money
  else:
      pass

# function to deduct the resources of order from resources of the machine.
def resources_left(coffee):
    for i in MENU[coffee]["ingredients"]:
        for r in resources:
            if r == i:
              resources[r] = resources[r] - MENU[coffee]["ingredients"][i]
    return resources

# main program starts
os.system('cls')
total_revenue = 0
machine_on = True
while machine_on == True:
  # input as the user chooses from the given list of coffee
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  
  if choice == "report":
    print()
    for r in resources:
      print(f"{r}: {resources[r]}")
    print(f"Total sale: ${total_revenue}")
    print()
  elif choice == "off":
    machine_on = False
  else:
    # checks resources are enough or not.
    check = check_resources(choice)
    for r in resources:
      if check == r:
        print(f"\nNot enough {r}")
        
        exit()
      else:
        pass
    
    # payment asked and checked payment is enough or not.
    payment = coins()
    cost = check_cost(choice)

    if cost == "\nnot enough payment":
      print(cost)
      exit()
    else:
      # change is given back to the user
      change = payment - MENU[choice]["cost"]
      total_revenue += MENU[choice]["cost"]
      print(f"\nYour change: ${round(change,2)}")
      resources_left(choice)
      print(f"\nHere's your {choice} sir. Thank you for choosing coffee machine.\n")
    
  
      
      

