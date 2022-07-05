members=['工藤','松田','浅木']
print(members[2])

members.append('菅原')
members.append('湊')
members.append('朝香')

print(members)

members.remove('湊')

print(members)

del members[2]
print(members)


scores=[89,90,95]

total=sum(scores)
print(f'合計{total}')

print(len(scores)) # 3

a=[10,20,30,40,50]
b=a[1:3]
print(b) #[20,30]
c=a[2:]
d=a[:3]
e=a[:]

print(a[-1]) #50

f=a[-2:] #[40,50]

g=a[::-1] #[50,40,30,20,10]
