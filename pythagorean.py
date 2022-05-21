temp = 0
i = 2
while True:
    if i + (i+1) + (i+2) == (i+3) ** 2:
        print(i * (i+1) * (i+2))
        break
    i += 1