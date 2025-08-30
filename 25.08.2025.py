def to_camel_case(s):
    temp = []
    while True:
        if " " not in s and "-" not in s and "_" not in s:
            temp.append(s)
            break

        for i in range(len(s)):
            if s[i] in (" ","-","_"):
                temp.append(s[:i].lower())
                break
        s = s[i+1:]

    for i in range(len(temp)):
        if i > 0:
            if temp[i] != "":
                temp[i] = temp[i].title()
    s = ""
    for i in range(len(temp)):
        if temp[i] != "":
            s += temp[i]
    return s

result = to_camel_case("hello world") #"helloWorld"
print(result)
result = to_camel_case("HELLO WORLD") #"helloWorld"
print(result)
result = to_camel_case("secret agent-X") #"secretAgentX"
print(result)
result = to_camel_case("FREE cODE cAMP") #"freeCodeCamp"
print(result)
result = to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and " \
"a_parrot_ _named- _squawk") #"yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk"
print(result)