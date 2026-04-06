import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','&','*','(',')']
print("Welcome to Password Generator!")
n_letters=int(input("How many letters do you want in your password?\n"))
n_numbers=int(input("How many numbers do you want in your password?\n"))
n_symbols=int(input("How many symbols do you want in your password?\n"))
password_list=[]
password=''
for i in range(n_letters):
    char=random.choices(letters)
    password_list+=char
for i in range(n_numbers):
    char=random.choices(numbers)
    password_list+=char
for i in range(n_symbols):
    char=random.choices(symbols)
    password_list+=char
random.shuffle(password_list)
for i in password_list:
    password+=i
print(password)

