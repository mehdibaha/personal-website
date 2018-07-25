import bs4
import requests
import yaml

from collections import defaultdict

# config yaml w/ default dict
from yaml.representer import Representer
yaml.add_representer(defaultdict, Representer.represent_dict)

# Constants
GITHUB_USERNAME = 'mehdibaha'
DEF_ICON = 'ga ga-github'
CATEGORIES = {
    '\U0001F468': 'Side projects',
    '\U0001F4BC': 'Work',
    '\U0001F4D1': 'Documentation',
    '\U0001F3EB': 'School',
}

def gen_projects():
    url = f'https://github.com/{GITHUB_USERNAME}?tab=repositories'
    html = requests.get(url).text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    sources = defaultdict(list)
    for repo in soup.find_all('li', {'itemprop': 'owns'}):
        tag = repo.find('a')
        name = tag.text.strip()
        description = repo.find('p').text.strip()
        # generate url
        url = tag.text[1:].strip()
        url = f'{GITHUB_USERNAME}/{url}' if '/' not in url else url
        url = f'https://github.com/{url}'
        # check if contains emoji at beginning
        if any(key in description for key in CATEGORIES.keys()):
            # retrieve category of repo based on emoji
            category = CATEGORIES.get(description[0]) 
            sources[category].append({'name': name, 'description': description, 'url': url})
    projects = {'name': 'Projects', 'source': sources}
    return projects

def main():
    projects = gen_projects()
    yaml.dump(projects, stream=open('data/projects.yml', 'w'), default_flow_style=False)

if __name__ == '__main__':
    main()

main()