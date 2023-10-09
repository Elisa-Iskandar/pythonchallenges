EXERCISE 1: Make your own list and print the first to fourth items with commas.
EXERCISE 2: Make a list of video game characters that you can input items into.
mylist = [0,1,2,3]
for x in mylist:
  print(x, end = ",")
print(" ")
characters = []
print("Enter -1 to stop entering characters.")
while True:
  temp = str(input("Character name: "))
  if temp != "-1":
    characters.append(temp)
  else:
    break
