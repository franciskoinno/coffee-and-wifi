import csv

with open('cafe-data.csv', 'a', newline='', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["form.cafe.data",
                     "form.location.data",
                     "form.open.data",
                     "form.close.data",
                     "form.coffee_rating.data",
                     "form.wifi_rating.data",
                     "form.power_rating.data"])

