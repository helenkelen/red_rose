

#create first project in py
#helevator with secret flour 
#with 1-9 flour are open for all people
#but 10 flour is close
#you need input password
#if flour is open you need show it user and if close too

#User write chooce number 
print("Write number your flour:")

usernumber = input()
#print("Your choice is: " + usernumber)

#if usernumber == "a":
#    print("a")
#else:
#    print("Five equal two")

#create secret code
secretcode = "123546"

#flour numbers
znumb = "0"
nnumb = "9"


#if, elif for user flour
if usernumber == znumb or usernumber == nnumb: 
  print("Welcome on 0 flour!")

elif usernumber == 10:
    userpassword = input("Please enter your code: ")
    if userpassword == secretcode:
        print("Welcome mr. John")
    else:
        print("Sorry, repeat do")

else:
    ("Sorry, uncorrect enter!")
