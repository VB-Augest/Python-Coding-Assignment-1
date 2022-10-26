L1 = []
L2 = [1,2,3,4,5]
i = 0
while i < 5:
  c = input("enter the elements")
  i=i+1
  L1.append(c)
A = {}
for key in L1:
    for value in L2:
        A[key] = value
        L2.remove(value)
        break
print("Resultant dictionary is : " + str(A))
