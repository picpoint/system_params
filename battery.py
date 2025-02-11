import psutil

def battery_params():
    print()
    print("------------Батарея------------")
    battery = psutil.sensors_battery()
    if str(battery) == "None":
        print("Заряд батареи не определён ... :-(")
    else:
        print(f"Заряд батареи {int(battery.percent)}%")
    print("-------------------------------")