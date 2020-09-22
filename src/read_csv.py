import csv
import projects_scrap

checked_repos = []
with open('qaward2020_projects.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if len(row) > 0:
            print(row[0])
            checked_repos.append(row[0])

if len(projects_scrap.candidate_repos) == len(checked_repos):
    print('all checked!')
print(f"checked: {len(checked_repos)} \n {checked_repos}")
