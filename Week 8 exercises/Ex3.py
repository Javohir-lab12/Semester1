def reformat_number(phone_number):
    cleaned_number = []
    for c in phone_number:
        if "0" <= c <= "9":
            cleaned_number.append(c)
    # return cleaned_number ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    n = len(cleaned_number)
    i=0
    while i<n :
        if n-i<4:
            break
        i += 3
        cleaned_number.insert(i,"-") #['1', '2', '3', '-', '4', '5', '-', '6', '7', '-', '8', '9']
        i += 1
    if len(cleaned_number)-i == 4:
        cleaned_number.insert(i+2 , "-")
    return "".join(cleaned_number)

print(reformat_number("123 456 789"))     # 9 digits -> 3-3-3
print(reformat_number("123-456-7890"))    # 10 digits -> 3-3-2-2 (4 remaining -> 2-2)
print(reformat_number("123 45 678"))      # 8 digits -> 3-3-2
print(reformat_number("12"))              # 2 digits -> 2
print(reformat_number("12345"))           # 5 digits -> 3-2
print(reformat_number("--1 23 4-5 6-7--")) # 7 digits -> 3-2-2 (4 remaining -> 2-2) 