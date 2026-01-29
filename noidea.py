pin= 1234

if pin==1234:
    print("1, balance inquiry 2, withdrawal")
    balance=10000
    options=int(input("choose an option (1 or 2);"))
    if options==1:
        print("your current balance is: $(balance)")
    elif options == 2:
        amount= int (input("enter the amount to withwarw: "))
        if amount<balance:
            print ("insuffiecient balance.")
        else:
            balance = amount
            print(f"please  collect your cash: (amount)")
            print(f"withdrawal successful, new balance: (balance)")
            print(f"thank you for using the atm")
    else:
        print("invalid option selected.")
        exit()
else:
    print("incorrect PIN. Access denied.")
    exit()
    