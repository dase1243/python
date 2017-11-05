a = input("Попробуйте угадать число: ")
num = 123
while True:
    if int(a) == num:
        print("Вы угадали")
        break
    elif int(a) > num:
        print("Надо меньше")
    elif int(a) < num:
        print("Надо больше")
    a = input("Попробуйте еще раз: ")
