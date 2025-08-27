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

        print(temp)

    numbers=temp
    return numbers

numbers = [11, 4, 10, 17, 2]
operators = ['*', '*', '%']
x=evaluate(numbers,operators)
