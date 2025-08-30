def find_duplicates(arr):
    non_duplicates = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                if arr[i] not in non_duplicates:
                    non_duplicates.append(arr[i])
                    
    for i in range(len(non_duplicates)):
        min_index = i

        for j in range(i+1,len(non_duplicates)):
            if non_duplicates[j] < non_duplicates[i]:
                min_index = j
        temp = non_duplicates[i]
        non_duplicates[i] = non_duplicates[min_index]
        non_duplicates[min_index] = temp

    arr = non_duplicates
    return arr

result = find_duplicates([1, 2, 3, 4, 5]) #[]
print(result)
result = find_duplicates([1, 2, 3, 4, 1, 2]) #[1, 2]
print(result)
result = find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2,
                           43, 2, 12, 0, 2, 4, 4]) #[-6, 0, 2, 4, 5, 23]
print(result)