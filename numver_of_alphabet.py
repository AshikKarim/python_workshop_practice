versity_name="Green University"
versity_name=versity_name.lower()
print(versity_name)
res =   {}
for i in range(0,len(versity_name)):
    if versity_name[i] in res:
        res[versity_name[i]]+=1
    else:
        res[versity_name[i]]=1

print(res)