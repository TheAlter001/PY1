# айдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


a=int(input("введите число "))


print(a//100 + a//10%10 + a%10)

# a//100 находим первое число
# a//10%10 находим 2-ое число
# a%10 находим 3-е число