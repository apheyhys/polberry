phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

second1 = ''.join(plist[1:3])
second1 = second1 + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(second1)