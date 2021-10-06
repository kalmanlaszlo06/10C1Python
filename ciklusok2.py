#Írasd ki a számokat -30 és 30 között ötösével (-30, -25, -20…)!
'''
for i in range(-30,30,5):
    print(i)
'''
#Írasd ki a 3 első tizenhét többszörösét! (3, 6, 9..)
'''
i=3
while i<60:
    print(i)
    i=i+3
'''

#Írasd ki 2 első tizenhat pozitív egész kitevőjű hatványát (2, 4, 8, 16, 32,…)
'''
for i in range(1,16):
    print(pow(2,i), end=" ")
''' 
'''
for i in range(1,17):
    print("2 a(z)",i,"hatványon:", pow(2,i))
'''

#Írasd ki a 7-es szorzótábla első 25 eleméből azokat, amik 4-gyel oszthatók. 
'''
for i in range(1,7*25+1):
    if i%4==0:
        print(i)
'''

#Írasd ki a 144 osztóit! 
'''
for i in range(1,145):
    if 144%i==0:
        print(i)
'''

#Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóit! 
'''
a=int(input("Kérek egy pozitív egész számot! a = "))
for i in range(1,a+1):
    if a%i==0:
        print(i)
'''

#Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóinak az összegét!
'''
a=int(input("Kérek egy pozitív egész számot! a = "))
osszeg=0
for i in range(1,a+1):
    if a%i==0:
        osszeg=osszeg+i
print("A(z)",a, "osztóinak összege", osszeg) 
'''
#Írasd ki azokat a kétjegyű számokat, amelyek számjegyeinek összege 10 (19 28 37 ...) 
#Írasd ki azokat a számpárokat, amelyek összege 18 (1 -17, 2 -16, …) 

#Írasd ki a nyolcas szorzótábla első tíz tagját egymás mellé!
'''
for i in range(1,81):
    if i%8==0:
        print(i, end=" ")
'''