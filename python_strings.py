#           01234567890123456789012345
#           65432109876543210987654321
alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet = ""

print('reverse - ', alphabet[::-1])   # Perfect idiom to reverse string


print('slices - ', alphabet[0:25:2])
print('reverse slices - ', alphabet[26:0:-2])

print('qpo - ', alphabet[16:13:-1])
# OR
print('qpo - ', alphabet[-10:-13:-1])


print('edcba - ', alphabet[-22:-27:-1])
# OR
print('edcba - ', alphabet[4::-1])


print('reverse last 8 chars - ', alphabet[:-9:-1])
# OR
print('reverse last 8 chars - ', alphabet[:17:-1])


print('first char - ', alphabet[:1])
# OR
print('first char - ', alphabet[0])  # throws exception if string is empty