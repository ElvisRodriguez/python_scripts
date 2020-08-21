files = []

with open("ubuntu-file-backup", "r") as file:
    for line in file.readlines():
        files.append(line.split("\t")[0])

with open("ubuntu-file-backup", "w") as file:
    for package in files:
        file.write("{}\n".format(package))
