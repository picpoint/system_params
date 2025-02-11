import psutil

def prosecces_list():
    print()
    print("-----------Процессы------------")
    process = psutil.process_iter()
    for i in process:
        print(f"PID: {i.pid}, Name: {i.name()}, Status: {i.status()}")
    print("-------------------------------")
