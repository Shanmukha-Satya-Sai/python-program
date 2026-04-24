a=input()
def is_palindrome(a):
    s=0
    e=len(a)-1
    while s<e:
        if a[s]!=a[e]:
            return "not a palindrome"
    return "palindrome"
is_palindrome(a)
