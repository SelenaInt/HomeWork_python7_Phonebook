from pathlib import Path
from os.path import exists
from CSV_creating import creating
from File_writing import writing_csv
from File_writing import writing_txt
from read_contact import read_contact


def button():   
    path = 'Phonebook.csv'
    valid = exists(path)
    if not valid:
        creating()

writing_csv()
writing_txt()

print('Ок. Данные записаны успешно. Давайте посмотрим весь список контактов\n' + '-' * 20)
read_contact()