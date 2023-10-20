def bill_tip(bill):
    tip = float(5/100 * (float(bill)))

    print(f"Your bill is {bill}")
    
    print(f"The tip is {tip}")
bill = float(input("Enter your bill: "))

bill_tip(bill)
