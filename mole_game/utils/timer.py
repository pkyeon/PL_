import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"{i}...", end="", flush=True)
        time.sleep(1)
    print()
