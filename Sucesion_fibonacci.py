num_uno, num_dos = 0, 1
while num_dos <= 1597:
    print(num_uno, num_dos, end = " ") # 0 1 1 2 3...
    num_uno = num_uno + num_dos
    num_dos = num_uno + num_dos 