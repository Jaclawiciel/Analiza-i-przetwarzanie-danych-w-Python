def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    return a

while True:
    try:
        n = int(input("Podaj n \n> "))
    except ValueError as err:
        print("O nie! Podałeś nieprawidłową liczbę. Spróbuj ponownie...")
        print("{}".format(err))
    else:
        print(fib(n))

    repeat = input("Powtórzyć? (y/n) \n> ")
    if repeat.lower() != "y":
        break
