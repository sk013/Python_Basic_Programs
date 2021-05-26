name = input("Enter your name ")
i = 0
tmp = ""
while i<len(name) :
    if name[i] not in tmp:
        tmp += name[i]
        print(f"{name[i]} = {name.count(name[i])}")
    i += 1