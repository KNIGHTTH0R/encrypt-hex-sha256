
#eded
#
# 0.1  —    New:    Dojście do podstawowej funkcjonalności
# 0.2  —    New:    Przepisanie na python 3.4


import csv
from tkinter import filedialog
from tkinter import *
import os
from passlib.hash import hex_sha256 as hex_sha256


ggBversion = "0.2"


def open_csv(title_text):
    # try:
        csv_data = []
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
            title="Otwórz plik do zaszyfrowania",
            filetypes=[("Wszystkie pliki", ".*"), ("CSV", ".csv")],
            parent=root
            )
        my_file = open(file_path, 'r')
        reader = csv.reader(my_file, delimiter=';', quoting=csv.QUOTE_NONE)
        print("\n\nLOADING %s\n\n" % file_path)
        for row in reader:
            csv_data.append(row)
        my_file.close()
        print("\n%s has been loaded" % title_text)
        return csv_data


def save_csv(data, file_path=""):
    pigi_list = []
    new_file = True
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        title="Zapisz zaszyfrowany plik",
        filetypes=[("Wszystkie pliki", ".*"), ("CSV", ".csv")],
        parent=root
        )

    if not ".csv" in file_path:
        file_path += ".csv"

    new_file = not os.path.isfile(file_path)


    my_file = open(file_path, 'w')

    for datarow in data:
        row = ";".join(datarow)
        row += "\n"
        my_file.writelines(row)

    my_file.close()
    print("RAPORT has been saved: %s" % file_path)



new_data = []
data_csv = open_csv("Data to Encrypt")
print(len(data_csv))
for row in data_csv:
    new_data.append([row[0], row[1], row[2], hex_sha256.encrypt(row[3])])
print(len(new_data))
save_csv(new_data)




