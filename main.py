#input a word
text=str(input("enter a string: "))

#reverse string
#using step value as -1 to iteratein reverse
revText= text[::-1]
text=revText

print("reverse of given string is:  ")
print(text)
