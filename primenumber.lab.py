def print_prime_numbers(n):
    i,j,flag=0,0,0
    print('Prime numbers between 1 and {} are:'.format(n))
    for i in range(1,n+1):
        if(i==1 or i==0):
            continue
        flag=1
        for j in range(2,((i//2)+1)):
            if(i%j==0):
                flag=0
                break
        if(flag==1):
            print(i,end=" ")
n=int(input("Enter the number "))
print_prime_numbers(n)