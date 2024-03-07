my_string = "abccba"
i=0
j=len(my_string)-1
is_palindrome = True

while i<j:
    if (my_string[i] == my_string[j]):
        i+=1
        j-=1
    else:
        is_palindrome=False
        break
if is_palindrome==True:
    print("str is palindrome")
else:
    print("str is not palindrome")