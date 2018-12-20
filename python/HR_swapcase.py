#Hacker Rank - swap case of letters

def swap_case(s):
    final = ""
    for i in s:
        if (96 < ord(i) < 123):
            final += i.upper()
        elif (64 < ord(i) < 91):
            final += i.lower()
        else: final += i 

    return final


s = "heLLo"
swap_case(s)