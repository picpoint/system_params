import sys
import psutil
import os


def battery_params():
    os.system('cls')
    print("------------Батарея------------")
    battery = psutil.sensors_battery()
    if str(battery) == "None":
        print("Заряд батареи не определён ... :-(")
    else:
        print(f"Заряд батареи {int(battery.percent)}%")
    print("-------------------------------")

    print("Вернуться в главное меню - q")
    print("Завершить программу - любая другая клавиша")
    print()
    key = input("Введите команду: ")
    if key == "q":
        os.system('cls')
        from main import main
        main()
    elif key != "q":
        sys.exit()