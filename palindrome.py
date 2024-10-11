input=input('Enter a string : ')
len=len(input)
is_palindeome=False

for i in range(len//2):
    if input[i]==input[len-i-1]:
       is_palindeome=True
       break
if is_palindeome:
    print('no. is  palindrome')
else:
    print('no is  not a palindrome')
