def decode(s):
    def find_innermost_arr(arr):
        innermost_left_paren_index = arr.rfind('(')
        if innermost_left_paren_index == -1:
            return ""

        innermost_right_paren_index = arr.find(')', innermost_left_paren_index)

        if innermost_right_paren_index == -1:
            return ""
        
        if arr[innermost_left_paren_index] == "(":
            innermost_arr=arr[(innermost_left_paren_index+1):(innermost_right_paren_index)]

            innermost_arr = list(innermost_arr)
            innermost_arr.reverse()

            arr = arr[0:innermost_left_paren_index]+"".join(innermost_arr)+arr[(innermost_right_paren_index+1):]
        return arr
    
    while "(" in s:
        s = find_innermost_arr(s)
    return s

result = decode("(f(b(dc)e)a)") #"abcdef"
print(result)
result = decode("((is?)(a(t d)h)e(n y( uo)r)aC)") #"Can you read this?"
print(result)
result = decode("f(Ce(re))o((e(aC)m)d)p") #"freeCodeCamp"
print(result)