#Enpotasyon modil pwodwi ak cart.
from boutik import cart
from boutik.products import pwod

#Mo byenvini ak afichay meni boutik la.
print("--------------Nou swete w pase yon bon moman nan boutik la!---------------")

print("\n                                 MENI           ")
print("\n                         1-Chache pwodwi")
print("                         2-We panye ak tout pri Total")
print("                         3-Femen")
print("\n")

#Enteraksyon itilizate ak boutik la kote l ap chwazi kotel vle antre.
choice=input("Fe yon chwa anndan meni an : ")

#Kondisyon ki pase selon chwa itilizate a fe.
if choice=="1":
    print(pwod())
elif choice=="2":
    print(cart())
elif choice=="3":
    print("\nMesi deske w te vizite boutik lan.\nFEN PWOGRAM!")
else:
    print("Ou fe yon chwa ki pa nan meni an.")

