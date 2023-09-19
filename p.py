#loop fo the letters
for x in "banana":
    print(x)

#Print only if 'free' is present:
txt = "The best things in life are free"
if "free" in txt:
    print("Yes, 'free' is present.") 

#print string with int
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))