def longStr():
    char=input("please enter a string: ").lower()
    longest=char[0]
    current=char[0]
    if char.isalpha():
        for char in char[1:]:
            if char >= current[-1]:
                current += char
                if len(current) > len(longest):
                    longest = current
            else:
                current = char
        print(f"longest substring is {longest}")
    else:
        print("Enter characters only")

longStr()