a=float(20.1545)
b=int(1134)
c="Maia"
d="Carla"
print('Real de A = :%.2f Inteiro de B =:%d '%(a,b))
print("--"*21)
print("strings primeira C =:%s segunda D =:%s"%(c,d))
print("--"*21)
print(f"usando format A= {a:.2f} B={b}  C={c:.8s} D={d}")
l=[1,2,3,4]
print(f"Lista e formatação")

print(f"{l[0]:1}",end="")
print(f"{l[1]:2}",end="")
print(f"{l[2]:5}",end="")

