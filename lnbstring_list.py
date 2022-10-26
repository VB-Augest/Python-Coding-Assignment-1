A = input(str(" write a sentence or para "))
B = A.split()
result = [x for x in B if len(x) >4]
print(result)
