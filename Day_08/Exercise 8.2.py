#Write your code below this line ๐
def prime_checker(number):
    check = 0
    for i in range(1, number):
        if number % i == 0:
            check += 1
    if check == 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
    
#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
