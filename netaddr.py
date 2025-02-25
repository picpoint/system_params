import sys
import psutil
import os


def netaddr_params():
    os.system('cls')
    print("--------Сетевые устройства--------")
    net_addr = psutil.net_if_addrs()
    for net_device in net_addr:
        print(f"Название сетевой карты: {net_device}")
        print(f"IP-address: {net_addr[net_device][1][1]}")
        print(f"NET-mask: {net_addr[net_device][1][2]}")
        print(f"MAC-address: {net_addr[net_device][0][1]}")
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