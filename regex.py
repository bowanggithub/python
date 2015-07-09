import re
print("Test: 010-12345")
m=re.match(r"^(\d{3})-(\d{3,8})","010-12345")
print(m.group(1),m.group(2))

t="19:05:30"
print("Test:",t)
m=re.match(r"^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$",t)
print(m.groups())


s1="someone@gmail.com"
s2="bill.gates@microsoft.com"
m=re.match(r"^[\w\.]*@\w*.com$",s1)
if m:
    print("%s match" %s1)
re.match(r"^[\w\.]*@\w*.com$",s2)
m=re.match(r"^[\w\.]*@\w*.com$",s2)
if m:
    print("%s match" %s2)

s3="<Tom Paris> tom@voyager.org"
m=re.match(r"^<[\w\s]+>\s\w*@\w*.\w*$",s3)
if m:
    print("%s match" %s3)
