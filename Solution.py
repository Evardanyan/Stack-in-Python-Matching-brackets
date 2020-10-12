text = input()
brackets = []
for letter in text:
    if letter == "(":
        brackets.append(letter)
    elif letter == ")":
        if brackets:
            brackets.pop()
        else:
            brackets.append(letter)
            break
print("ERROR" if brackets else "OK")
