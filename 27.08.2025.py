def evaluate(numbers, operators):

    temp=numbers[0]

    for indeks in range(len(numbers)):
        if indeks == (len(numbers)-1):
            break
        operator_indeks=indeks%(len(operators))
        indeks = indeks+1

        if operators[operator_indeks] == "+":
            temp+=numbers[indeks] 
        elif operators[operator_indeks] == "-":
            temp-=numbers[indeks]
        elif operators[operator_indeks] == "*":
            temp*=numbers[indeks]
        elif operators[operator_indeks] == "/":
            temp/=numbers[indeks]
        elif operators[operator_indeks] == "%":
            temp%=numbers[indeks]

    numbers=int(temp)
    return numbers

result = evaluate([5, 6, 7, 8, 9], ['+', '-']) #3
print(result)
result = evaluate([17, 61, 40, 24, 38, 14], ['+', '%']) #38
print(result)
result = evaluate([20, 2, 4, 24, 12, 3], ['*', '/']) #60
print(result)
result = evaluate([11, 4, 10, 17, 2], ['*', '*', '%']) #30
print(result)
result = evaluate([33, 11, 29, 13], ['/', '-']) #-2
print(result)