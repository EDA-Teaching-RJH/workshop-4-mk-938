def coin_machine(total):
    payed = 0
    change = 0
    print ("Your total is £", total)
    while payed < total:
        coin = input("Please insert coin (1p, 2p, 5p, 10p, 20p, 50p, £1, £2)"))
        if coin == "1p"
        elif coin == "2p"
        elif coin == "5p"
        elif coin == "10p"
        elif coin == "20p"  

        else:
            print ("That was not a valid denomination")
    change = payed - total
    print ("Thank you, your total is:", change)

total = 0

print ("Welcome to the drink machine")
selection = int(input("""
1. Coffee -- £1.50
2. Coke -- £1.80
3. Tea -- £1.20
4. Water -- £0.80
Which item would you like; 1, 2, 3 or 4?: """))

match selection:
    case 1:
        print ("""
Would you like any sugar, milk or an extra shot?
1. sugar --- 20p
2. milk --- 20p
3. extra shot --- 50p
4. none""")
        extra = int(input("Enter 1, 2, 3 or 4"))
        match extra:
            case 1:
                total = 170
                coin_machine(total)
            case 2:
                total = 170
                coin_machine(total)
            case 3:
                total = 200
                coin_machine(total)
            case 4:
                total = 150
                coin_machine(total)
    case 2:
        total = 1.80
        coin_machine(total)
    case 3:
        total = 120
        coin_machine(total)
    case 4:
        total = 0.80
        coin_machine(total)        
