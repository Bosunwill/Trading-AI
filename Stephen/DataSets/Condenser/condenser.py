import csv
import os
from datetime import datetime


correctedRow = []
directory = 'TickerFiles'
 
for filename in os.listdir(directory):
    # read csv file as a list of lists
    with open(f"{directory}/{filename}", 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        list_of_rows = list(csv_reader)
        del list_of_rows[0]
        print(len(list_of_rows))
        for row in range(len(list_of_rows)):
            rowDate = list_of_rows[row][0]
            rowDate = rowDate.split('/')
            rowDate = rowDate[2] + '-' + rowDate[0] + '-' + rowDate[1]
            date_time_obj = datetime.strptime(rowDate, '%Y-%m-%d')
            if date_time_obj.weekday() == 0 or date_time_obj.weekday() == 6 or 'nan' in list_of_rows[row]:
                continue
            maxAcceptedValue = 500
            if float(list_of_rows[row][8]) > maxAcceptedValue or float(list_of_rows[row][9]) > maxAcceptedValue or float(list_of_rows[row][10]) > maxAcceptedValue or float(list_of_rows[row][11]) > maxAcceptedValue or float(list_of_rows[row][12]) > maxAcceptedValue or float(list_of_rows[row][13]) > maxAcceptedValue or float(list_of_rows[row][14]) > maxAcceptedValue or float(list_of_rows[row][15]) > maxAcceptedValue or float(list_of_rows[row][16]) > maxAcceptedValue or float(list_of_rows[row][17]) > maxAcceptedValue or float(list_of_rows[row][18]) > maxAcceptedValue or float(list_of_rows[row][19]) > maxAcceptedValue or float(list_of_rows[row][20]) > maxAcceptedValue or float(list_of_rows[row][21]) > maxAcceptedValue:
                continue
            list_of_rows[row][8] = float(list_of_rows[row][8]) - float(list_of_rows[row][5])
            list_of_rows[row][9] = float(list_of_rows[row][9]) - float(list_of_rows[row][5])
            list_of_rows[row][10] = float(list_of_rows[row][10]) - float(list_of_rows[row][5])
            list_of_rows[row][11] = float(list_of_rows[row][11]) - float(list_of_rows[row][5])
            list_of_rows[row][12] = float(list_of_rows[row][12]) - float(list_of_rows[row][5])
            list_of_rows[row][13] = float(list_of_rows[row][13]) - float(list_of_rows[row][5])
            list_of_rows[row][14] = float(list_of_rows[row][14]) - float(list_of_rows[row][5])
            list_of_rows[row][15] = float(list_of_rows[row][15]) - float(list_of_rows[row][5])
            list_of_rows[row][16] = float(list_of_rows[row][16]) - float(list_of_rows[row][5])
            list_of_rows[row][17] = float(list_of_rows[row][17]) - float(list_of_rows[row][5])
            list_of_rows[row][18] = float(list_of_rows[row][18]) - float(list_of_rows[row][5])
            list_of_rows[row][19] = float(list_of_rows[row][19]) - float(list_of_rows[row][5])
            list_of_rows[row][20] = float(list_of_rows[row][20]) - float(list_of_rows[row][5])
            list_of_rows[row][21] = float(list_of_rows[row][21]) - float(list_of_rows[row][5])
            list_of_rows[row][22] = float(list_of_rows[row][22]) - float(list_of_rows[row][5])
            correctedRow.append(list_of_rows[row])


with open("out.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(correctedRow)
