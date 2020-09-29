def horizonlen(R,h):
    H=(R+h)**2-(h**2)
    H=H**0.5
    return H



def HorCalc(m, h, bh, r, planet ):
    man = horizonlen(r,m)
    house = horizonlen(r,h)
    BH = horizonlen(r,bh)
    print(man, house, BH,"-",planet)


HorCalc(0.002,0.03,0.828,6371, "Earth")
HorCalc(0.002,0.03,0.828,3389,"mars")



# def even(m, h, bh, planet):
#     man = ((((m + planet) ** 2) - (planet ** 2)) ** 0.5)
#     house = ((((h + planet) ** 2) - (planet ** 2)) ** 0.5)
#     BH = ((((bh + planet) ** 2) - (planet ** 2)) ** 0.5)
#     print(man, house, BH,"-Венера")
even(0.002,0.03,0.828,6051)

# def even(m, h, bh, planet):
#     man = ((((m + planet) ** 2) - (planet ** 2)) ** 0.5)
#     house = ((((h + planet) ** 2) - (planet ** 2)) ** 0.5)
#     BH = ((((bh + planet) ** 2) - (planet ** 2)) ** 0.5)
#     print(man, house, BH,"-Юпитер")
even(0.002,0.03,0.828,69911)

# def even(m, h, bh, planet):
#     man = ((((m + planet) ** 2) - (planet ** 2)) ** 0.5)
#     house = ((((h + planet) ** 2) - (planet ** 2)) ** 0.5)
#     BH = ((((bh + planet) ** 2) - (planet ** 2)) ** 0.5)
#     print(man, house, BH,"-Меркурий")
even(0.002,0.03,0.828,2439)

# def even(m, h, bh, planet):
#     man = ((((m + planet) ** 2) - (planet ** 2)) ** 0.5)
#     house = ((((h + planet) ** 2) - (planet ** 2)) ** 0.5)
#     BH = ((((bh + planet) ** 2) - (planet ** 2)) ** 0.5)
#     print(man, house, BH,"-Сатурн")
even(0.002,0.03,0.828,58232)


# def even(m, h, bh, planet):
#     man = ((((m + planet) ** 2) - (planet ** 2)) ** 0.5)
#     house = ((((h + planet) ** 2) - (planet ** 2)) ** 0.5)
#     BH = ((((bh + planet) ** 2) - (planet ** 2)) ** 0.5)
#     print(man, house, BH,"-Нептун")
even(0.002,0.03,0.828,24622)

# def even(m, h, bh, planet):
#     man = ((((m + planet) ** 2) - (planet ** 2)) ** 0.5)
#     house = ((((h + planet) ** 2) - (planet ** 2)) ** 0.5)
#     BH = ((((bh + planet) ** 2) - (planet ** 2)) ** 0.5)
#     print(man, house, BH,"-Уран")
even(0.002,0.03,0.828,25362)

# def even(m, h, bh, planet):
#     man = ((((m + planet) ** 2) - (planet ** 2)) ** 0.5)
#     house = ((((h + planet) ** 2) - (planet ** 2)) ** 0.5)
#     BH = ((((bh + planet) ** 2) - (planet ** 2)) ** 0.5)
#     print(man, house, BH,"-Плутон")
even(0.002,0.03,0.828,1188)

print("Дополнительно: ")

# def even(m, h, bh, planet):
#     man = ((((m + planet) ** 2) - (planet ** 2)) ** 0.5)
#     house = ((((h + planet) ** 2) - (planet ** 2)) ** 0.5)
#     BH = ((((bh + planet) ** 2) - (planet ** 2)) ** 0.5)
#     print(man, house, BH,"-Луна")
even(0.002,0.03,0.828,1737)

# def even(m, h, bh, planet):
#     man = ((((m + planet) ** 2) - (planet ** 2)) ** 0.5)
#     house = ((((h + planet) ** 2) - (planet ** 2)) ** 0.5)
#     BH = ((((bh + planet) ** 2) - (planet ** 2)) ** 0.5)
#     print(man, house, BH,"-Солнце")
even(0.002,0.03,0.828,696340)
