def battle(my_army, opposing_army):
    length_my_army = len(my_army)
    length_opposing_army = len(opposing_army)
    battle_result = []

    if length_my_army == length_opposing_army:
        my = 0
        opposing = 0

        for i in range(length_my_army):
            if str.isdigit(my_army[i]):
                my = my_army[i]
            elif str.isalnum(my_army[i]) == False:
                my = 0
            else:
                my = ord(my_army[i])

            if str.isdigit(opposing_army[i]):
                opposing = opposing_army[i]
            elif str.isalnum(opposing_army[i]) == False:
                opposing = 0
            else:
                opposing = ord(opposing_army[i])

            battle_result.append(int(my)-int(opposing))

        my_result = 0
        opposing_result = 0
    
        for i in battle_result:
            if i < 0:
                opposing_result +=1
            elif i > 0:
                my_result +=1

        print(my_result,opposing_result)
        
        if my_result > opposing_result:
            my_army = "We won"
        elif my_result < opposing_result:
            my_army = "We lost"
        else:
            my_army = "It was a tie"

    elif length_my_army > length_opposing_army:
        my_army = "Opponent retreated"
    elif length_my_army < length_opposing_army:
        my_army = "We retreated"

    return my_army

result = battle("C@T5", "D0G$")
print(result)