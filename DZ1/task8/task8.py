# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

n=int(input("введите длину "))
m=int(input("введите ширину "))
k=int(input("введите колличиство долек "))

if k%n == 0 or k%m == 0:    #что бы узнать можно ли разделить ровно, нужно что бы хоть одна из частей делилась
    print("Разломим")
else: 
    print("Целиком не получится")

