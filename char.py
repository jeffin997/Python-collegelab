strl=input("enter the string:")
print("original string:",strl)
char=strl[0]
strl=strl.replace(char,'$')
strl=char+strl[1:]
print("replace string:",strl)
