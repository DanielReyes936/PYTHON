def progression_type(a, b, c):
    if (c-b) == (b-a):
        common_diff = c-b
        progression_type = 'Arithmetic Progression'
        next_member = c + common_diff
    elif (c/b) == (b/a):
        common_ratio = c/b
        progression_type = 'Geometric Progression'
        next_member = c * common_ratio
    else:
        return "Not a valid progression"

    return progression_type, next_member

# test the function with some sample inputs
a = 3
b = 5
c = 7
progression_type, next_member = progression_type(a, b, c)
print("The progression type is: ", progression_type)
print("The next successive member is: ", next_member)
