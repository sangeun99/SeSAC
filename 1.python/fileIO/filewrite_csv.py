# csv : comma seperated value

import csv

data = [
    ("name", "age", "city"),
    ("john", 23, "Seoul"),
    ("emily", 55, "Busan"),
    ("peter", 25, "Seoul"),
    ("sam", 64, "Daegu")
]

with open("user.csv", "w", newline = "") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)