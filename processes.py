import sys
import psutil
import os


def prosecces_list():
    os.system('cls')
    print("-----------Процессы------------")
    process = psutil.process_iter()
    for i in process:
        print(f"PID: {i.pid}, Name: {i.name()}, Status: {i.status()}")
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