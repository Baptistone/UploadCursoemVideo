from time import sleep
for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
    if c == 0:
        print('BOOM!!')
