import sys
import psutil
import os


def memory_params():
    os.system('cls')
    print("----------Параметры ОЗУ---------")
    memory = psutil.virtual_memory()
    total_memory = memory.total / 1000000000
    print(f"Оперативная память - {int(total_memory)}Гб")

    free_memory = str(memory.available / 1024 / 1024 / 1024)[:3]
    print(f"Свободная память - {free_memory}Гб")

    used_memory = str(memory.used / 1024 / 1024 / 1024)[:3]
    print(f"Использованно - {used_memory}Гб")


    swap = psutil.swap_memory()
    swap_memory = str(swap.total / 1024 / 1024 / 1024)[:3]
    print(f"Общая память подкачки - {swap_memory}Гб")

    swap_used = str(swap.used / 1024 / 1024 / 1024)[:3]
    print(f"Используемая память подкачки - {swap_used}Гб")

    swap_free = str(swap.free / 1024 / 1024 / 1024)[:3]
    print(f"Свободная память подкачки - {swap_free}Гб")
    print("-------------------------------")

    print("Вернуться в главное меню - q")
    print("Завершить программу - любая другая клавиша")
    print()
    key = input("Введите команду: ")
    if key == "q":
        os.system('cls')
    elif key != "q":
        sys.exit()
