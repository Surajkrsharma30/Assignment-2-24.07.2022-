#write a python programme to print a dictionary whose key should be alphabet from a-z and the value should be corresponding ASCII values.
#sample output:-{'a',97,'b',98,'c',99,'d',100,'e',101,'f',102,'g',103,'h',104,'i',105,'j',106,'k',107,'l',108,'m',109,'n',110,'o',111,'p',112,'q',113,'r',114,
# 's',115,'t',116,'u',117,'v',118,'w',119,'x',120,'y',121,'z',122} in dictionary

#create the dictionary
dict={}
for i in range(97,97 + 26):#alphabet charecter from a to z ranging
    dict[chr(i)]=i  #chr() function represent the  unicode.
#print the value in dictionary
print(dict,end="\n\t\t\t\t\t\t\t\tthank you sir\n")
