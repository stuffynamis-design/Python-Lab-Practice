digit={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"voilet":7,"grey":8,"white":9}
multiplier={"black":1,"brown":10,"red":100,"orange":1000,"yellow":10000,"green":100000,"blue":1000000,"voilet":10000000,"grey":100000000,"white":1000000000}
print("the all colors")
print("black brown red orange yellow green blue voilet grey white")
brand1=(input("Enter brand 1 value:".lower()))
brand2=(input("Enter brand 2 value:".lower()))
brand3=(input("Enter brand 3 value:".lower()))
value=(((digit[brand1]*10)+digit[brand2])*multiplier[brand3])
print("the value of the resistor:",value)
