#divid numbers
num = 32 - 4
print(num)

#if method
if 5 > 2:
    print("Five if greater than two!")

#create first project in py
#helevator with secret flour 
#with 1-9 flour are open for all people
#but 10 flour is close
#you need input password
#if flour is open you need show it user and if close too

#User write chooce number 
usernumber = input("Write number your flour: ")
print("Your choice is: " + usernumber)

#create secret code
secretcode = 123546

#flour numbers
znumb = 0
nnumb = 9

#if, elif for user flour
if usernumber > znumb and usernumber < nnumb:
    print("Welcome!")

elif usernumber == 10:
    userpassword = input("Please enter your code: ")
    if userpassword == secretcode:
        print("Welcome mr. John")
    else:
        print("Sorry, repeat do")

else:
    ("Sorry, uncorrect enter!")
