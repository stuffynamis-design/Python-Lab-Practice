units=float(input("Enter the unit:"))
if(units<=100):
    bill=units*1.5
elif(units<=200):
    bill=(100-1.5)*((units-1.5)*2.5)
bill=(100*1.5)+(100*2.5)+((units-200)*4)
print ("Electricity bill in Rs", bill)