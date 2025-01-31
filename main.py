import psutil

# cpu_load = psutil.cpu_percent(interval=1, percpu=True)
# print(f"Количество ядер - {len(cpu_load)}")
#
# for kernel in cpu_load:
#     print(f"Загрузка {cpu_load.index(kernel) + 1}-го ядра {kernel} %")
#
# cpu_frequency = psutil.cpu_freq()
# print(f"Частота процессора - {cpu_frequency.max / 1000} ГГц")


# memory = psutil.virtual_memory()
# total_memory = memory.total / 1000000000
# print(f"Оперативная память - {int(total_memory)}Гб")
#
# free_memory = str(memory.available / 1024 / 1024 / 1024)[:3]
# print(f"Свободная память - {free_memory}Гб")
#
# used_memory = str(memory.used / 1024 / 1024 / 1024)[:3]
# print(f"Использованно - {used_memory}Гб")


# swap = psutil.swap_memory()
# swap_memory = str(swap.total / 1024 / 1024 / 1024)[:3]
# print(f"Общая память подкачки - {swap_memory}Гб")
#
# swap_used = str(swap.used / 1024 / 1024 / 1024)[:3]
# print(f"Используемая память подкачки - {swap_used}Гб")
#
# swap_free = str(swap.free / 1024 / 1024 / 1024)[:3]
# print(f"Свободная память подкачки - {swap_free}Гб")

disk_partitions = psutil.disk_partitions(all=False)
print("Устройства в системе:")

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


