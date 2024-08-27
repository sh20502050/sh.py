def bank_system():
    
  print("********************* hi ******************* ")
  print(" *********** welcome to our bank *********** ")
  balance= float(input( "your balance:  "))
    
  while True:
    print(" choicd operat  :")
    print("1. rassed ")
    print("2. sa7b")
    print("3. eda3")
    print ("4. foaed")
    print("5. exit")

    choice = float(input(" operat  no: "))

    if choice == 1:
        print("  balance:$", balance)
    elif choice == 2:
       amount = float(input("    money to take: "))
       if amount <= balance:
        balance -= amount
        print("  acount money:$", balance)
       else:
        print("  no balance.$")
    elif choice == 3:
      amount = float(input("    money you want to input: "))
      balance += amount
      print("    account money:$", balance)
    elif choice == 4:
      amount = float (input  (" foaed %:  "))
      balance2= balance* amount/100
      print(f"   arba7 :$ {balance2}")
      total= balance+balance2
      print ("   total:$",total)
    elif choice == 5:
      print("    thanx.")
      break
    else:
      print("   input true operation no.")

bank_system()
    
