import csv
import os

fieldnames = ["name of file", "image_url"]
os.chdir(r'''$''')

for each_file in os.listdir():

    results = []

    with open(str(each_file), "r") as read_file:
        reader = csv.DictReader(read_file, fieldnames = fieldnames)
        for each_row in reader:
            results.append(each_row)

    with open(str(each_file), "w", newline="") as write_file:
        writer = csv.DictWriter(write_file, fieldnames = fieldnames)
        writer.writeheader() #writes out the header rows to the csv file.
        for each_row in results:
            writer.writerow(each_row)


# Another way of writing


# fieldnames = ["name of file", "image_url"]
# results = []

# with open("tps_report.csv", "r") as read_file:
#     reader = csv.DictReader(read_file, fieldnames = fieldnames)
#     for each_row in reader:
#         results.append(each_row)

# # print(results)

# with open("tps_report.csv", "w", newline="") as write_file:
#     writer = csv.DictWriter(write_file, fieldnames = fieldnames)
#     writer.writeheader() #writes out the header rows to the csv file.
#     for each_row in results:
#         writer.writerow(each_row)


# Another way of writing


# fieldnames = ["name of file", "image_url"]
# results = []
# dictionaries_in_list = []

# with open("tps_report.csv", "r") as read_file:
#     reader = csv.reader(read_file)
#     for each_row in reader:
#         results.append(each_row)

# for each_list in results:
#     dictionaries_in_list.append({"name of file": each_list[0], "image_url": each_list[1]})

# with open("tps_report.csv", "w", newline="") as write_file:
#     writer = csv.DictWriter(write_file, fieldnames = fieldnames)
#     writer.writeheader() #writes out the header rows to the csv file.
#     for each_dictionary in dictionaries_in_list:
#         writer.writerow(each_dictionary)
