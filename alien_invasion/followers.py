import requests

url = "https://api.github.com/users/torvalds"
response = requests.get(url)
print(f'Response code: {response.status_code}')
response_dict = response.json()
print(f'response_dict keys: {response_dict}')
repo_dicts = response_dict['items']
print(f'repo_dicts keys: {len(repo_dicts)}')