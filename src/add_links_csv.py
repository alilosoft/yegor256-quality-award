import csv
import projects_scrap

repos = []
with open('qaward2020_projects_nolinks.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        if len(row) > 0:
            row[0] = 'https://github.com/'+row[0]
            repos.append(row)


with open('qaward2020_projects_link.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    for row in repos:
        csv_writer.writerow(row)

print(f"checked: {len(repos)} \n {repos}")
