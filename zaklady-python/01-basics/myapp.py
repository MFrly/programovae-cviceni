x = 10
print("Zahrajeme si kvíz!!!")
print("Víš kolik je 1 + 1?")
print(":")
answer=input()
if answer == 2:
    print("Ne tohle neni sprava odpoved")
else:
    print("Ne tohle neni sprava odpověď")

print("Zkuse něco podobného.")
print("Když do dvou litrového kyblíku neleješ tři sta mililtrů vody.")
print("Kolik máš kyblíků?")
answer_2=input()
if int(answer_2) == 1:
       print("Tohle už máš správně!!!!")
       print("Dobře zkusme to naposledy.")
       print("Napis cislo {}".format(x))
       answer_3 = input()
       if int(answer_3) == x:
           print("No super!!!")
           print("Nazdar!")

       else:
           print("Thole je konec")
else:
       print("Tohle bylo fakt jednoduché!!!")
       print(answer_2)

print("Tak někdy příště!!!")
