arr = [0, 0, 1, 0, 0, 0, 1, 1, 1]

# [0,0,0,0,1,1,1,1,1]

left = 0
right = len(arr) - 1

while left < right:
    if arr[left] == 1 and arr[right] == 0:
        # swap
        arr[left], arr[right] = arr[right], arr[left]
    if arr[left] == 0:
        left += 1
    if arr[right] == 1:
        right -= 1

print(arr)
