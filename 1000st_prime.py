n_prime = 2
count = 0
temp = 0
prime = []
while len(prime) <= 751:
    i = 2
    isPrime = True
    while i < n_prime:
        if n_prime % i == 0:
            isPrime = False
            break
        i += 1
    if isPrime is True:
        prime.append(n_prime)
        count += 1
        print(n_prime, 'Position at:', count)
    n_prime += 1
print(prime[len(prime)-1])
print('='*100)
for i in prime:
    temp += i
    print(temp)
if temp < 2000000:
    print('Less than two million')

# testing git pull

