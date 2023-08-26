import glob

myfiles = glob.glob("files/*.txt")
print(myfiles)

for filepath in myfiles:
    with open(filepath, "r") as file_local:
        print(file_local.read())