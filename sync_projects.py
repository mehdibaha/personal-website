import bs4
import requests
import ruamel.yaml
import sys

GITHUB_USERNAME = 'mehdibaha'
DEF_ICON = 'ga ga-github'

url = f'https://github.com/{GITHUB_USERNAME}'
html = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser')

projects = {'name': 'Projects'}
sources = []

for repo in soup.find_all('li', {'class': 'pinned-repo-item'}):
	tag = repo.find_all('a', {'class': 'text-bold'})[0]
	# finding name
	name = tag.find_all('span', {'class': 'repo'})[0].text
	name = name.capitalize()
	# finding description
	description = repo.find_all('p', {'class': 'pinned-repo-desc'})[0].text
	description = f'{description[1:]}'
	# finding url
	url = tag.text[1:-1]
	url = f'{GITHUB_USERNAME}/{url}' if '/' not in url else url
	url = f'https://github.com/{url}'
	# adding complete repo
	sources.append({'name': name, 'description': description, 'url': url, 'icon': DEF_ICON})
projects['source'] = sources

yaml = ruamel.yaml.YAML()
yaml.dump(projects, open('data/projects.yml', 'w'))
