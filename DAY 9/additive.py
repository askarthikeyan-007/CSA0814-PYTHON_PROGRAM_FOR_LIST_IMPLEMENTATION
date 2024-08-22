
box = []

while True:
    inp = input("Enter number for the sequence (enter * to stop):\n")
    if inp == '*':
        break
    if inp.isdigit():  
        num = int(inp)
        box.append(num)
    else:
        print("Please enter a valid non-negative integer or '*' to stop.")

if len(box) >= 3:
    additive = True
    for i in range(len(box) - 2):
        if box[i] + box[i + 1] != box[i + 2]:
            additive = False
            break

    if additive:
        print("It is an additive sequence.")
    else:
        print("It is not an additive sequence.")
else:
    print("Please enter at least three numbers.")
