import csv


def read_contact():
    file = 'Phonebook.csv'
    with open(file, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            item = ', '.join(row)
            print(item)
            print()
        print('End of contacts\n' + '-' * 20)

