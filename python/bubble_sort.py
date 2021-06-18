array = [4, 7, 2, 8, 3, 1, 8, 9, -2, 12, -3, -5]

def sort(arr):
  for _ in range(len(arr) - 1):
    for index in range(len(arr) - 1):
      current = arr[index]
      next = arr[index + 1]
      
      if (current > next):
        arr[index + 1] = current
        arr[index] = next

  return arr
      
sort(array)
print(array)