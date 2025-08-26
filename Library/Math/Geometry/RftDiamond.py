import os


os.system("cls")


def rft_diamond():
    h = 5
    y = int(h / 2)
    a = True
    for i in range(h):
        x = ""
        for j in range(h):
            if j == y or j == h - 1 - y:
                x += "*"
            else:
                x += " "
        if y > 0 and a:
            y -= 1
        else:
            a = False
            y += 1
        print(x)


rft_diamond()
