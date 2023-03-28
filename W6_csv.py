import csv

def reading ():
    with open("student.csv") as students:
        csv_reader = csv.reader(students)
        next(csv_reader) #Progresses the lines in CSV (remove headers)
        for row in csv_reader:
            print(f"{row[0]} received marks of {row[2]}, {row[3]}")