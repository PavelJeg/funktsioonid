#Üleasanne N.16





#While True:
    #g = input("mis number ma arvasin?(1-10, mängu lõpetamiseks kirjutage *lõpp*  )  n")
    #if g.lower() =="lõpp":
        #print("mäng on läbi!")
        #break
    #if not g.isnumeric():
        #print("Vale andmetüüp!")
        #continue
    #g = int(g)
    #if g == ans:
        #print("õige! sa arvasid ära!")
        #break
        #breakif g>10 or g<1:
            #print("Vahemik on vale!")
            #continue
        #elf g !=ans:
            #print("vale!proovi veel karra! numbri oli {ans}")




#Ülesanne 3
#try:
    #f = int(input("mitu ülesandeid sa tahad? "))
    #for d in range (0,f,1):
        #print("ülesanne: ")
        #a = randint(1,50)
        #b = randint(1,50)
        #c = a+ b
        #for i in range (0,5,1):
            #answer = int (input(f"{a}+{b}=? "))
            #if answer == a+b:
                #print("see on õige")
                #break
            #else:
                #print("Proovi veel karra")
                #print()
        #g = g+1
        #print(f"õige on {c} ")
#except:
    #print("see ei ole õige")


    #Ülesanne 13


    #print("arv", "  ruut ", "   kuup")
    #for i in range(1, 11):
    #    # print( i ,i**2 , i**3 )
    #    print(f" {i}     {i**2}      {i**3}")
    #    print("teine variant")
    ##Ülesanne 13-2

    #    print("arv" , "  ruut ", "  kuup")
    #    i = 1
    #    while i < 11:
    #        print(f" {i}    {i**2}          {i**3}) 
    #        i += 1
     

    #import string
    #import random

    #print("Arva taht - (from Aa to Zz)")
    #letter = random.choice(string.ascii_letters

    #While True:
    #    answ = str(input("Teie oletus:"))
    #    if letter == answ:
    #    print("Tubli!")
    #    break
    #else: print("Provi uuesti!")


    #Ülesanne 22

    #while True:
    #    print("Tahan kammi!")
    #    if a =="komm" and a == "KOMM":
    #        print("Aitah! Oli vaja " + str(n) + "Katse"
    #              break
    #          else:
    #              n = n + 1


#Ülesanne 6

#print()
#print("Ülesanne 6 1")
#print()
#for i in range(0,5):
#    print("* "*5)
#print()
#for i in range(0,10):
#    print("* "*i)
#print()
#for i in range(0,10):
#    print("* "*(10-i))
#print()


#Ülesanne 1

#print()
#print("Ülesanne 0 1")
#print()
#kujund=input("")

#Ülesanne 8

#While True
#   try:
#       mainnumber = int(input("Vali number 1-100"))
#       break
#   except ValueError:
#       print("See pole täisarv")
#   if mainnumber<1 or mainnumber>100:
#       print("Vali õige number")
#   else:
#       paaris = 0
#       paaritu = 0
#       x = paaris
#       while x != mainnumber:
#           x = x +1
#           print(int(x), end=" ")
#           if x % 2 == 0:
#               paaris += 1
#            else:
#                paaritu += 1

    
#    print("Paaris numbrid", paaris)
#    print("Paaritu numbrid") paaritu



#from random import *
#n=randint(1,10)
#While True:
#    text = input("Väljumiseks sisetage number : ")
#    a+=1
#    if text == "stopp":
#        print("Välju programmist! Kohtumiseni! See sai tehtud",n)
#        break 
#    elif int(text) == n:
#        print("palju õnne, sa võitsid")
#        break
#    else:
#        print("proovi veel korra")
#    if a == 3:
#        print("")
#        break


While True:
    UserName = input("Sisesat kasutajanimi: ")
    PassWord = input("Siseta parool: ")

    if UserName == "Edvard" and Password == "123":

        time.sleep(1)
        print("Kõik on korras!")
        time.sleep(1)
        print("Sa võid tööle asuda.")
        break
    else:
        print ("Viga!")
