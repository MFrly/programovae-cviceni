x = 10
print("Zahrajeme si kvíz!!!")
print("Víš kolik je 1 + 1?")
print(":")
answer = input()

if answer == "2":
    print("Ano, to je správná odpověď!")
else:
    print("Ne, tohle není správná odpověď.")

print("Zkusme něco podobného.")
print("Když do dvou litrového kyblíku naliješ tři sta mililitrů vody, kolik máš kyblíků?")
answer_2 = input()

if int(answer_2) == 1:
    print("Tohle už máš správně!!!!")
    print("Dobře, zkusme to naposledy.")
    print(f"Napiš číslo {x}.")
    answer_3 = input()

    if int(answer_3) == x:
        print("No super!!!")
        print("Nazdar!")
    else:
        print("Tohle je konec.")
else:
    print("Tohle bylo fakt jednoduché!!!")
    print(answer_2)

print("Tak někdy příště!!!")
