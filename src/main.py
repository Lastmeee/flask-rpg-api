import time

count = 0

while True:
    print("Hello world")
    count += 1
    key = input()
    if key == 'w':
        print(f"Message was printed {count} times.")
        break