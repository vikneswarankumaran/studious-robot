import os
empty_files = open(r'''$''', "a")

os.chdir(r'''$''')

for each_file in os.listdir():
    with open(str(each_file), "r", encoding="utf8") as read_file:
        if len(read_file.read()) == 0:
            file_name = str(each_file)
            empty_files.write(f"{file_name} is an empty text file in JSPA.")
            empty_files.write("\n")
        else:
            pass

empty_files.close()
