import sys
import psutil
import os


def hd_params():
    os.system('cls')
    print("--------Параметры диска--------")
    disk_partitions = psutil.disk_partitions(all=False)
    for dev in disk_partitions:
        print(f"Диск {dev[0]} - {dev[2]}")
        try:
            disk_volume = psutil.disk_usage(f"{dev[0]}")
            print(f"Полный объём диска {dev[0]} - { str(disk_volume[0] / 1024 / 1024 / 1024)[:5]}Гб")
            print(f"Занято {dev[1]} - {str(disk_volume[1] / 1024 / 1024 / 1024)[:5]}Гб")
            print(f"Свободно {dev[2]} - {str(disk_volume[2] / 1024 / 1024 / 1024)[:5]}Гб")
        except BaseException as err:
            print(f"Не возможно определить объём диска {dev[0]}")
        print()
    print("-------------------------------")

    print("Вернуться в главное меню - q")
    print("Завершить программу - любая другая клавиша")
    print()
    key = input("Введите команду: ")
    if key == "q":
        os.system('cls')
    elif key != "q":
        sys.exit()