from random import *
import os
str1 = '1234567890'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
str4 = '!@#$%^&*()'
str0 = '<>/\|~-_=+{}[]::""'
str5 = str1 + str2 + str3 + str4 + str0


rrr = list(str5)

shuffle(rrr) 

password = "".join([choice(rrr) for i in range(35)])


log = input("Enter your Login:")
print(log)
print("  /\ ")
print("   | this is you login use this to reg.")
print(password)
print("   /\  ")
print("   |  This is your password, and this safe just copy he and paste for reg.")


q = ("password = " + password + " " + "login = " + log)
print(q)
os.system('touch login.txt')

file = open ("login.txt", "w")
file.write(q)
print("Ok your file with login and password already on this direcroty keep this file(his name'login.txt')")
