A=[0,64,128,192]
B=[]
for i in A:
  for j in range(i,i+64):
    B.append(chr(j))
print(B)
