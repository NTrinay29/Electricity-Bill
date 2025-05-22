units = float(input())
bill = 0
if units <= 50:
    bill = units*2
elif 50<units<=150:
    bill += 50*2
    bill = bill + (units-50)*3
elif 150<units<=250:
    bill += 100*3 + 100
    bill = bill + (units-150)*5
elif units>250:
    bill += 100*5 + 400
    bill = bill + (units-250)*8

bill += bill*0.2
print(bill)
