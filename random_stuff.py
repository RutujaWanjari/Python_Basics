# FORMAT

# If you want to print something in different lines without using \n use triple quote
print("""hello
hello
hello
hello""")
print("""
Jan : {2}
Feb : {0}
Mar : {2}
Apr : {1}
May : {2}
Jun : {1}
""".format(28,30,31))
print('')

# Need to think a lot for formatting
for i in range(1, 5):
    print("No.", i, "squared is", i**2, "and cubed is", i**3)
print('')

# Too much error prone
for i in range(1, 5):
    print("No. " + str(i) + " squared is " + str(i**2) + " and cubed is " + str(i**3))
print('')

# Easy as cakewalk and can be used in more complex problems
for i in range(1, 11):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))
print('')

# More formatting
for i in range(1, 11):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))
print('')

# More formatting
for i in range(1, 11):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))