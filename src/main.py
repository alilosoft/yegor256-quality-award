import requests
import time
import csv
import projects_scrap
import os
import read_csv

# get all projects from https://www.yegor256.com/2019/11/03/award-2020.html
html = requests.get('https://www.yegor256.com/2019/11/03/award-2020.html')


# print(html.text)


# get HoC: https://hitsofcode.com/github/<user>/<repo>/json
def hoc(repo):
    hoc_req = requests.get(f'https://hitsofcode.com/github/{repo}/json')
    return hoc_req.json()['count']


# get LoC: https://api.codetabs.com/v1/loc/?github==<username>/<reponame>
def codetabs_loc_json(repo):
    loc_req = requests.get(f'https://api.codetabs.com/v1/loc/?github={repo}')
    return loc_req.json()


# TODO: check if json contains the keys
def loc_languages(loc_json):
    langs = ''
    for lang in loc_json:
        langs += f"{lang['language']}({lang['linesOfCode']}) "
    return langs


def loc_total(loc_json):
    return loc_json[len(loc_json) - 1]['linesOfCode']  # last item in json is the total of all languages


# check age > 1y: https://api.github.com/repos/<user>/<repo>/commits?until=2019-09-01
# https://api.github.com/repos/cybercog/laravel-love
def github_info(repo):
    token = os.getenv('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'}
    gh_req = requests.get(f'https://api.github.com/repos/{repo}', headers=headers)
    json = gh_req.json()
    return {
        'lang': json['language'],
        'created': json['created_at'][0:10]
    }


def age(repo, until='2019-09-01'):
    commits = requests.get(f'https://api.github.com/repos/{repo}/commits?until={until}')
    if len(commits.json()) > 0:
        # commit_date = commits.json()[0]['commit']['author']['date'][0:10]
        # print(f'1Y+ Commit: {commit_date}')
        return '> 1 year'
    else:
        return '< 1 year'


print(age('fleksl/avatar-maker'))


def write_csv():
    # load already processed repos
    checked_repos = read_csv.checked_repos
    current = len(checked_repos)
    # scrap repos from html
    # repos = projects_scrap.candidate_repos
    repos = ["chaqmoq/chaqmoq", "chaqmoq/http", "retejs/rete"]
    proj_count = len(repos)

    fields = ['Repo', 'Lang', 'LoC', 'HoC', 'Created', 'Age', 'LoC/Lang']
    with open('qaward2020_projects.csv', mode='a+', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()

        for repo in repos:
            if repo in checked_repos:
                current += 1
                continue
            try:
                print("")
                gh_info = github_info(repo)
                print(f"Github: {gh_info}")
                gh_lang = gh_info['lang']
                gh_created = gh_info['created']
                age_v = age(repo)
                print(f"Age: {age_v}")
                codetabs_loc = codetabs_loc_json(repo)
                loc_lang = loc_languages(codetabs_loc)
                loc_v = loc_total(codetabs_loc)
                print(f"LoC: {loc_v}")
                hoc_v = hoc(repo)
                print(f"HoC: {hoc_v}")
                # csv row
                repo_dic = {
                    'Repo': 'https://github.com/' + repo,
                    'Lang': gh_lang,
                    'LoC': loc_v,
                    'HoC': hoc_v,
                    'Created': gh_created,
                    'Age': age_v,
                    'LoC/Lang': loc_lang
                }
                # csv
                writer.writerow(repo_dic)
                current += 1
                print('--------------------------')
                print(f"#{current}/{proj_count} {repo}, {gh_lang}, {loc_v}, {hoc_v}, {gh_created}, {age_v}, {loc_lang}")
            except Exception:
                print(f'Error checking repo:{repo}')
            finally:
                print('--------------------------')
                time.sleep(6)  # API wait
