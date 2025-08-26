import os

# clear screen
os.system("cls")

# get working directory and filename
cwd = f"{os.getcwd()}/RftData/CP/AdventOfCode/Templates/"
filename = f"{cwd}AdventOfCodeProblemNames.txt"

cwd_target_dir = f"{os.getcwd()}/RftCP/AdventOfCode/"
cwd_target_dir_io = f"{os.getcwd()}/RftData/CP/AdventOfCode/IO/"

# store data from file in a list
a = open(filename, "r").read().splitlines()
a = [i for i in a if i]
# a = list(filter(None, a))


def clean_filenames():
    a[0] = a[0].replace("\ufeff", "")
    a.sort()
    open(filename, "w").writelines(a)


def create_puzzles():
    file_list = os.listdir(cwd_target_dir)
    template = open(f"{cwd}RftAdventOfCodeCodeFileTemplate.txt", "r").read()

    for i in range(0, len(a)):
        if not file_list.__contains__(f"{a[i]}.py"):
            b = a[i].replace("\n", "")
            with open(f"{cwd_target_dir}{b}.py", "w") as file:
                file.writelines(template.replace("[x]", b))
                pass


def create_io():
    file_list = os.listdir(cwd_target_dir_io)

    for i in range(0, len(a)):
        if not file_list.__contains__(f"{a[i]}_Input.txt"):
            b = a[i].replace("\n", "")
            with open(f"{cwd_target_dir_io}{b}_Input.txt", "w") as file:
                pass
        if not file_list.__contains__(f"{a[i]}_Output.txt"):
            b = a[i].replace("\n", "")
            with open(f"{cwd_target_dir_io}{b}_Output.txt", "w") as file:
                pass


# clean_filenames()
# create_puzzles()
# create_io()
