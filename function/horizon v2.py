def horizonlen(R,h):
    H=(R+h)**2-(R**2)
    H=H**0.5
    return H

def HorCalc(r, planet ):
    man = horizonlen(r,0.002)
    house = horizonlen(r,0.03)
    BH = horizonlen(r,0.828)
    print(man, house, BH,"-",planet)


HorCalc(6371, "Earth")
HorCalc(3389,"mars")

