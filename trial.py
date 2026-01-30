l1 = ["math", "English", "Informatics", "Chemistry"]
l2 = ["today", "tomorow"]
print(type(l2))
l2p = ["yesterday"] + l2
l2.insert(1, "yesterday")
l3 = ["monday", "tuesday"]

liste = []

liste.append(l1)
print(liste)

liste.append(l2)
print(liste)

liste.append(l2p)
print(liste)