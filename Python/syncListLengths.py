listA = ["a","b","c","d","e","f","s","t","u","v"]
listB = ["h","i","j","k","l","m","n","o","p","q","r"]

length = 0

if len(listA) >= len(listB):
    length = len(listA)
else:
    length = len(listB)

for count in range(length):
    if count >= len(listA):
        listA.append("+")
    else:
        listB.append("+")
    print("A : {}, B : {}".format(listA[count], listB[count]))