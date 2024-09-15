first = int(input("Введите первое число "))
print(first)
second = int(input("Введите второе число "))
print(second)
trird = int(input("Введите третье число "))
print(trird)
if first == second and first ==trird:
    print(3)
elif first == second or first == trird:
    print(2)
else:
    print('Равных чисел нет')

