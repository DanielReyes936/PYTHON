# input the heights of eight buildings
heights = []
for i in range(8):
    height = int(input(f"Enter height of building {i+1}: "))
    heights.append(height)

# sort the list in descending order
heights.sort(reverse=True)

# print the heights of the top three buildings
print("Heights of the top three buildings:")
for i in range(3):
    print(heights[i])


