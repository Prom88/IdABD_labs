def grade(score):
    if score > 100 or score < 0:
        print("отчислен")
        return 0
    if score > 90:
        print("отлично")
    elif score > 74:
        print("хорошо")
    elif score > 60:
        print("удовлетворительно")
    elif score > 0:
        print("неудовлетворительно")


grade(101)
