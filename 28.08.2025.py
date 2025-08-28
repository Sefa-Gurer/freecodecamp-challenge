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

laptops = [1500, 2000, 1800, 1400]
budget = 1900
# budget = 1700
# budget = 1300
result = get_laptop_cost(laptops, budget)
print(result)
