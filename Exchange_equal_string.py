str1="aaa3acd=bbb5679909090ab"
pos=str1.find("=")
print(str(str1.find("=")))
print(str(str1.split("=")))
list=str(str1.split("="))
print (list[2:pos+2])
print (list[pos+6:len(list)-2])
print (str(list[pos+6:len(list)-2])+"="+str(list[2:pos+2]))