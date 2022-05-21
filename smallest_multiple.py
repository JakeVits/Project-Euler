num = 2520
found, run = True, True
while run:
    print(num)
    for i in range(1, 21):
        if num % i != 0:
            found = False
            break
    if found is True:
        run = False
    else:
        found = True
        num += 2
print(num)
