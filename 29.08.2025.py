def burn_candles(candles, leftovers_needed):

    total_burned = candles
    leftover = candles

    while leftover >= leftovers_needed:
        new_candles = int(leftover / leftovers_needed)
        total_burned += new_candles 
        leftover = new_candles+(leftover % leftovers_needed)
        candles = leftover

    candles = total_burned
    return candles

result = burn_candles(7, 2) #3
print(result)
result = burn_candles(10, 5) #12
print(result)
result = burn_candles(20, 3) #29
print(result)
result = burn_candles(17, 4) #22
print(result)
result = burn_candles(2345, 3) #3517
print(result)