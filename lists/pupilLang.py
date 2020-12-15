l1={"E","G","F"}
l2={"G","E"}
l3={"F","E","I"}

#языки, которые знают все ученики - пересечение
commonLang=l1&l2
commonLang=commonLang&l3
print(commonLang)

#языки, которые знает хотя бы один ученик - объединение
allLang=l1|l2
allLang=allLang|l3
print(allLang)