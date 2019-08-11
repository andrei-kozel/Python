import csv

my_list = [["Top Gun", "Risky Business", "Minority Report"], [
    "Titanic", "The Revenant", "Inception"], ["Trainig Day", "Man on Fire", "Flight"]]


with open('3.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=',')
    for line in my_list:
        w.writerow(line)
