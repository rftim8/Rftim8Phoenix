import os


os.system("cls")


def rft_polynomial():
    fa = "y = 20x + 7"
    fb = "y = 49x + 12"

    f1 = fa.split("=")[1]
    f2 = fb.split("=")[1]

    x1 = f1.split(" ")[1]
    x2 = f2.split(" ")[1]

    y1 = f1.split(" ")[3]
    y2 = f2.split(" ")[3]

    a = int(x1.replace("x", "")) - int(x2.replace("x", ""))
    b = int(y2) - int(y1)

    x = b / a
    y = int(x1.replace("x", "")) * x + int(y1)

    r = f"({'%.2f' % x},{'%.2f' % y})"

    print(r)


rft_polynomial()
