import psutil

def netaddr_params():
    print()
    print("--------Сетевые устройства--------")
    net_addr = psutil.net_if_addrs()
    for net_device in net_addr:
        print(f"Название сетевой карты: {net_device}")
        print(f"IP-address: {net_addr[net_device][1][1]}")
        print(f"NET-mask: {net_addr[net_device][1][2]}")
        print(f"MAC-address: {net_addr[net_device][0][1]}")
        print()
    print("-------------------------------")