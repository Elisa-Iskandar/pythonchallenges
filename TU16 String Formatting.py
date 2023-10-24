#Exercise 1:  Create a float variable for Ringgit and print it as "RM129"
Ringgit = float(129)
print("RM", Ringgit)

#Exercise 2: Create a table of numbers with headings
numcol1 = [7.953955544,
           9.169702197,
           17.716042768]
numcol2 = [76.771408830,
          27.084024527,
          8.210451384]
numcol3 = [84.166282148,
          22.291120765,
          84.851503603]

print("header?")
for x in range(3):
  print(f"{numcol1[x]:<9} {numcol2[x]:<9} {numcol3[x]:<9}")

#Exercise 3: Create a quick binary convertor
number = int(123)
print(bin(number))
