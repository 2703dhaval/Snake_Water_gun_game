"""
print("enter your first number ")
num1 = int(input())

print("enter your second number ")
num2 = int(input())

print("choise operator *, + , / , - , ")
operator = (input())

if num1 == 45 and num2 == 3 and operator == "*":
    print(555)

elif num1 ==  56 and num2 == 9 and operator == "+":
    print(77)

elif num1 == 56 and num2 == 6 and operator == "/":
    print(4)

elif operator == "*":
    num4 = num1 * num2
    print(num4)

elif operator == "+":
    num5 = num1 + num2 
    print(num5)

elif operator == "/":
    num6 = num1 / num2
    print(num6)   

elif operator == "-":
    num7 = num1 - num2
    print(num7)  

else:
    ("error please check your input")  
"""   
"""           
print("enter your first number ")
num1 = int(input())

print("enter your second number ")
num2 = int(input())

print("choise operator *, + , / , - , ")
operator = (input())

if num1 == 45 and num2 ==3 and operator == "*":
    print(555)
elif num1 == 56 and num2 == 9 and operator == "+":
    print(77)
elif num1 == 56 and num2 == 6 and operator == "/":
    print(4)
elif operator == "*":
    print(num1 * num2)   
elif operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 + num2)
elif operator == "/":
    print(num1 / num2)
else:
    ("error please check your input")
"""
"""
print("new iphone 14  model")
iphone = ["iphone 14 , iphone 14 plus , iphone 14 pro , iphone 14 pro max"]
print(iphone) 
iphone = int(input("enter your buget ")) 

if iphone < 50000:
    print("your buget in not buy iphone 14")
elif iphone < 70000:
    print("your buget in iphone 14")
elif iphone < 90000:
    print("your buget in 2 iphone iphone 14 and iphone 14 plus your choise")
elif iphone < 115000:
    print("your buget in 3 iphone 14 , 14 plus and 14 pro  your choise")
elif iphone < 130000:
    print("your buget in 4 iphone 14 , 14 plus ,14 pro , 14 pro max")  
else:
    print("check your input and try agin")  
"""
"""
cartype = ["suv" , "sedan", "luxury", "sport car"]
print(cartype)
for car in cartype:
    carx = (input("enter your car type "))
    if carx == cartype[0]:
        print("suv car in harrier,creta,fortunar,xuv700 and much more")
    elif carx == cartype[1]:
        print("sedan car in honda city,verna,slaviya,virtus,ciaz and much more")    
    elif carx == cartype[2]:
        print("bmw,rang rover,mercedes bens,porsche,audi and much more")
    else:
        print("check your input and try agin")  
"""

iphone = ["iphone11","iphone11promax","iphone12","iphone12promax",
           "iphone13","iphone13promax","iphone14","iphone14promax"]
print(iphone) 
for phone in iphone:
    buget = (int(input("enter your buget ")))
    if buget < 50000:
        print("your buget in only iphone11 and 11promax")
    elif buget < 81000:
        print("your buget in ihphone 11,11promax,12 and 12promax") 
    elif buget < 95000:
        print("your buget in iphone 11,11promax,12,12promax,13 and 13promax")  
    else:
        print("your buget in all iphone")         


   






  


