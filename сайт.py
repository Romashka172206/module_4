def naoborot(a):
    return a[::-1]==a

while True:
    a=input("Введите слово: ")
    print(f"{a} True" if
    naoborot(a) else "False")