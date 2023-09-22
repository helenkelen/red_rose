"""
caffee program
shop market 
you need add products ad get check
"""
#Creatings in check
print("Welcome to the clothe shop!")
print("Your order are:")

#equal
print("All sum is")

#product code
c_1, c_2, c_3, c_4, c_5, c_6 = "12", "11", "10", "9", "6", "7"

#product list
p_1, p_2, p_3, p_4, p_5, p_6  = "Jack T-shirt", "M pants", "H dress", "N jacket", "f jeans", "red dress"

#product cost
c_1, c_2, c_3, c_4, c_5, c_6 = 23, 12, 11, 123, 5, 60 

#loop for order product
def order():
    empl = input("Write code for product.")

    if empl == c_1:
        print(p_1)

    if empl == c_2:
        print(p_2)

    if empl == c_3:
        print(p_3)

    if empl == c_4:
        print(p_4)

    if empl == c_5:
        print(p_5)

    if empl == c_6:
        print(p_6)

order()

"""#loop for cost product
def order():
    empl = int(input("Write code for product."))

    if empl == c_1:
        print(p_1)

    if empl == c_2:
        print(p_2)

    if empl == c_3:
        print(p_3)

    if empl == c_4:
        print(p_4)

    if empl == c_5:
        print(p_5)

    if empl == c_6:
        print(p_6)"""