def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # x is present at mid
        else:
            return mid
 
    # If we reach here, x is not present
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 6

# Function call
result = binary_search(arr, x)

if result != -1:
    print(f"Element is present at index {str(result)}")
else:
    print("Element is not present in array")
