

#create first project in py
#helevator with secret flour 
#with 1-9 flour are open for all people
#but 10 flour is close
#you need input password
#if flour is open you need show it user and if close too

#User write chooce number 
print("Write number your flour:")

usernumber = input()


#create secret code
secretcode = "123546"


#1 - 9 flour
if usernumber == "1":
  print("Welcome on the 1 flour!")

elif usernumber == "2":
  print("Welcome on the 2 flour!")

elif usernumber == "3":
  print("Welcome on the 3 flour!")
  
elif usernumber == "4":
  print("Welcome on the 4 flour!")
  
elif usernumber == "5":
  print("Welcome on the 5 flour!")
  
elif usernumber == "6":
  print("Welcome on the 6 flour!")
  
elif usernumber == "7":
  print("Welcome on the 7 flour!")
  
elif usernumber == "8":
  print("Welcome on the 8 flour!")
  
elif usernumber == "9":
  print("Welcome on the 9 flour!")

else:
   print("Sorry, uncorrect!")
  


if usernumber == "10":
    userpassword = input("Please enter your code: ")
    if userpassword == secretcode:
        print("Welcome mr. John")
    else:
        print("Sorry, repeat do")

else:
    ("Sorry, uncorrect enter!")
