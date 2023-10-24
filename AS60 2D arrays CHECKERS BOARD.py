#Given two numbers nn and mm. Create a two-dimensional array of size (n×m)(n×m) and populate it with the characters "." and "*" in a checkerboard pattern. The top left corner should have the character "."
m = 5
n = 5
arr = []
for row in range(m):
  r = []
  for col in range(n):
    if row%2==0:
      if col%2==0:
        r.append("*")
      else:
        r.append(".")
    else:
      if col%2==0:
        r.append(".")
      else:
        r.append("*")
  arr.append(r)
print(arr)
