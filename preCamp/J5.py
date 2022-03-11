from sample_package import logarithm

logarithm()


with open("note.txt", "r") as f:
    for line in f.readlines():
        print(line, end="")
