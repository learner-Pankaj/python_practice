
lang = ('python', 'java', 'c++')
lis = list(lang)
lis[1] = 'javascript'
tup = tuple(lis)
print(tup)

#tuple can't be updated
#tuple can only be updated in the way is convert it into list and update the tuple and again convert it into tuple and print
coordinate = (10,20)
(x, y) = coordinate #remeber always number of argument should be the same if not * have to be used
print(x)
print(y)
