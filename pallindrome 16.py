a=input('enter your number : ')
palindrome=True
for i in range(len(a)//2):
    if a[i]!=a[len(a)-i-1]:
        palindrome=False

if palindrome is True:
    print('palindrome')
else:
    print('not a palindrome')