l = [3, 1, 4, 6, 5]

for i in l:
  squared = [x ** 2 for x in l]
    # Step 2: Sort the squared array
  squared.sort()

  n = len(squared)

    # Step 3: Fix one element (as c²) and use two pointers for a² + b² = c²
  for i in range(n - 1, 1, -1):  # i is the index of c²
        left = 0
        right = i - 1

        while left < right:
            if squared[left] + squared[right] == squared[i]:
                # Convert back to original numbers
                a = int(squared[left] ** 0.5)
                b = int(squared[right] ** 0.5)
                c = int(squared[i] ** 0.5)
                
                break
            elif squared[left] + squared[right] < squared[i]:
                left += 1
            else:
                right -= 1
print(f"Pythagorean Triplet Found: {a}, {b}, {c}")