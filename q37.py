#Write a program to rotate a list by k positions.(clockwise)
l=list(map(int,input().split()))
k=int(input())
c=0
while c<2:
        t=l.pop()
        l.insert(0,t)
        c+=1
        print(l)

# #Write a program to rotate a list by k positions.(anticlockwise)
# l = list(map(int, input().split()))
# k = int(input())
# c = 0
# while c < k:
#     t = l.pop(0)      # remove first element
#     l.append(t)       # insert at end
#     c += 1
#     print(l)
#
# #Write a program to print all rotations of a list (clockwise)
# l = list(map(int, input().split()))
# n = len(l)
# c = 0
# while c < n:
#     t = l.pop()        # take last element
#     l.insert(0, t)     # move to front
#     print(l)
#     c += 1
#
# #Write a program to print all rotations of a list (anticlockwise)
# l = list(map(int, input().split()))
# n = len(l)
# c = 0
# while c < n:
#     t = l.pop(0)     # remove first element
#     l.append(t)      # add to end
#     print(l)
#     c += 1