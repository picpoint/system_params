from cpu import cpu_params
from memory import memory_params
from hd import hd_params
from netaddr import netaddr_params
from processes import prosecces_list
from battery import battery_params


print("------Выберите пункт меню------")
print("[1] Параметры процессора")
print("[2] Параметры ОЗУ")
print("[3] Параметры жёсткого диска")
print("[4] Параметры сетевой карты")
print("[5] Параметры процессов")
print("[6] Параметры заряда батареи")
print("-------------------------------")

command = input("Введите команду: ")

def main(command):
    if command == "1":
        cpu_params()
    elif command == "2":
        memory_params()
    elif command == "3":
        hd_params()
    elif command == "4":
        netaddr_params()
    elif command == "5":
        prosecces_list()
    elif command == "6":
        battery_params()
    else:
        print("Введена неправильная команда... :-(")



if __name__ == '__main__':
    main(command)




