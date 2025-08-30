def get_laptop_cost(laptops, budget):
    for i in range(len(laptops)):
        max_index = i

        for j in range(i+1,len(laptops)):
            if laptops[j] > laptops[max_index]:
                max_index = j
                
        temp = laptops[i]
        laptops[i] = laptops[max_index]
        laptops[max_index] = temp

    if laptops[-1] > budget:
        laptops = 0
    elif budget > laptops[1]:
        laptops = laptops[1]
    else:
        for i in range(len(laptops)):
            if budget > laptops[i]:
                laptops = laptops[i]
                break
    return laptops

result = get_laptop_cost([1500, 2000, 1800, 1400], 1900) #1800
print(result)
result = get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900) #1800
print(result)
result = get_laptop_cost([2099, 1599, 1899, 1499], 2200) #1899
print(result)
result = get_laptop_cost([2099, 1599, 1899, 1499], 1000) #0
print(result)
result = get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450) #1400
print(result)