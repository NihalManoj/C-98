def swap_file():
    with open("A.txt", "r") as A:
        dataA = A.read()
    with open("B.txt", "r") as B:
        dataB = B.read()
    with open("A.txt", "w") as A:
        A.write(dataB)
    with open('B.txt', "w") as B:
        B.write(dataA)
swap_file()