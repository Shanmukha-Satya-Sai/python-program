n=10
word="x"
while len(word)<=n:
    s=""
    for i in word:
        if i=='z':
            n_w='a'
        else:
            n_w=chr(ord(i)+1)
        s+=n_w
    word+=s
    print(word)
print(word[n-1])