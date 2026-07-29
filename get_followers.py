import requests

url = "https://api.github.com/users/torvalds"
headers = {"Accept": "application/vnd.github.v3+json"}
proxies = {"http": "http://127.0.0.1:33210", "https": "http://127.0.0.1:33210"}

r = requests.get(url, headers=headers, proxies=proxies)
print(f"Status code: {r.status_code}")

user_dict = r.json()
print(f"Followers: {user_dict['followers']}")
