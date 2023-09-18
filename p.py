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
usernumber = input("Write number your flour.")
print("Your choice is: " + usernumber)

#if, elif for user flour
if usernumber > 0 and usernumber < 9:
    print("Welcome!")

elif usernumber == 10:
    print("Please enter your code: ")

else:
    ("Sorry, uncorrect enter!")
