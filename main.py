import psutil
from cpu import cpu_params

command = input("Введите команду: ")

def main(command):
    if command == "1":
        cpu_params()

if __name__ == '__main__':
    main(command)



#
# disk_partitions = psutil.disk_partitions(all=False)
# print("Устройства в системе:")
# print("--------------------")
#
# for dev in disk_partitions:
#     print(f"Диск {dev[0]} - {dev[2]}")
#     try:
#         disk_volume = psutil.disk_usage(f"{dev[0]}")
#         print(f"Полный объём диска {dev[0]} - { str(disk_volume[0] / 1024 / 1024 / 1024)[:5]}Гб")
#         print(f"Занято {dev[1]} - {str(disk_volume[1] / 1024 / 1024 / 1024)[:5]}Гб")
#         print(f"Свободно {dev[2]} - {str(disk_volume[2] / 1024 / 1024 / 1024)[:5]}Гб")
#     except BaseException as err:
#         print(f"Не возможно определить объём диска {dev[0]}")
#     print()
#
#
#
# net_addr = psutil.net_if_addrs()
# print("Сетевые устройства:")
# print("--------------------")
#
# for net_device in net_addr:
#     print(f"Название сетевой карты: {net_device}")
#     print(f"MAC-address: {net_addr[net_device][0][1]}")
#     print(f"IP-address: {net_addr[net_device][1][1]}")
#     print(f"NET-mask: {net_addr[net_device][1][2]}")
#     print()
#
#
# print()
# print("Процессы:")
# print("--------------------")
# process = psutil.process_iter()
#
# for i in process:
#     print(f"PID: {i.pid}, Name: {i.name()}, Status: {i.status()}")
#
# print()
# print("--------------------")
# battery = psutil.sensors_battery()
#
# if str(battery) == "None":
#     print("Заряд батареи не определён ... :-(")
# else:
#     print(f"Заряд батареи {int(battery.percent)}%")