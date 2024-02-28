#A painter wants to know what size to make his paintings, she's heard of this golden ratio, but doesn't know how to calculate it. Given a length can you calculate the height for a landscape.
golden_ratio = (1+(5)**(0.5))/2
length = int(input("Input length: "))
height = length/golden_ratio
print(height)
