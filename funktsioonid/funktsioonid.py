#�leasanne N.16





#While True:
    #g = input("mis number ma arvasin?(1-10, m�ngu l�petamiseks kirjutage *l�pp*  )  n")
    #if g.lower() =="l�pp":
        #print("m�ng on l�bi!")
        #break
    #if not g.isnumeric():
        #print("Vale andmet��p!")
        #continue
    #g = int(g)
    #if g == ans:
        #print("�ige! sa arvasid �ra!")
        #break
        #breakif g>10 or g<1:
            #print("Vahemik on vale!")
            #continue
        #elf g !=ans:
            #print("vale!proovi veel karra! numbri oli {ans}")




#�lesanne 3
#try:
    #f = int(input("mitu �lesandeid sa tahad? "))
    #for d in range (0,f,1):
        #print("�lesanne: ")
        #a = randint(1,50)
        #b = randint(1,50)
        #c = a+ b
        #for i in range (0,5,1):
            #answer = int (input(f"{a}+{b}=? "))
            #if answer == a+b:
                #print("see on �ige")
                #break
            #else:
                #print("Proovi veel karra")
                #print()
        #g = g+1
        #print(f"�ige on {c} ")
#except:
    #print("see ei ole �ige")


    #�lesanne 13


    #print("arv", "  ruut ", "   kuup")
    #for i in range(1, 11):
    #    # print( i ,i**2 , i**3 )
    #    print(f" {i}     {i**2}      {i**3}")
    #    print("teine variant")
    ##�lesanne 13-2

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


    #�lesanne 22

    #while True:
    #    print("Tahan kammi!")
    #    if a =="komm" and a == "KOMM":
    #        print("Aitah! Oli vaja " + str(n) + "Katse"
    #              break
    #          else:
    #              n = n + 1


#�lesanne 6

#print()
#print("�lesanne 6 1")
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


#�lesanne 1

#print()
#print("�lesanne 0 1")
#print()
#kujund=input("")

#�lesanne 8

#While True
#   try:
#       mainnumber = int(input("Vali number 1-100"))
#       break
#   except ValueError:
#       print("See pole t�isarv")
#   if mainnumber<1 or mainnumber>100:
#       print("Vali �ige number")
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
#    text = input("V�ljumiseks sisetage number : ")
#    a+=1
#    if text == "stopp":
#        print("V�lju programmist! Kohtumiseni! See sai tehtud",n)
#        break 
#    elif int(text) == n:
#        print("palju �nne, sa v�itsid")
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
        print("K�ik on korras!")
        time.sleep(1)
        print("Sa v�id t��le asuda.")
        break
    else:
        print ("Viga!")
