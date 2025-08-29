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

candles, leftovers_needed = 7, 2
result = burn_candles(candles, leftovers_needed)
print(result)