n =int(input())
i = 2
while i<= (n-1):
    if n%i == 0:
        print("non_prime")
        exit()
    else:
        i +=1
print("prime")