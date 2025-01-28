import psutil

# cpu_load = psutil.cpu_percent(interval=1, percpu=True)
# print(f"Количество ядер - {len(cpu_load)}")
#
# for kernel in cpu_load:
#     print(f"Загрузка {cpu_load.index(kernel) + 1}-го ядра {kernel} %")


cpu_frequency = psutil.cpu_freq()
print(f"Частота процессора - {cpu_frequency.max / 1000} ГГц")