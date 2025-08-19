def тыры_пыры():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("тыры-пыры")
        elif i % 3 == 0:
            print("тыры")
        elif i % 5 == 0:
            print("пыры")
        else:
            print(i)

тыры_пыры()
