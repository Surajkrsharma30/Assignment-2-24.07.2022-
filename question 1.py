#write a python program to get list,sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# sample list:-[(2,5),(1,2),(4,4),(2,3),(2,1)].
# Expected output:-[(2,1),(1,2),(2,3),(4,4),(2,5)]

l = [(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in range (len(l)):
    for j in range (len(l)):
      if l[i][1] < l[j][1]:
         l[i],l[j] = l[j],l[i]
print(l,end="\n\t thank you sir\t\t")


