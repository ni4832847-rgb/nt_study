import requests

# 执行API调用并查看响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+stars:>10000&sort=stars&order=desc"

headers = {"Accept":"application/vnd.github.v3+json"}
proxies = {"http": "http://127.0.0.1:33210", "https": "http://127.0.0.1:33210"}
r = requests.get(url, headers=headers, proxies=proxies)
print(f"Status code: {r.status_code}")

# 将响应转为字典
response_dict = r.json()

# 处理结果
# print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results:{not response_dict['incomplete_results']}")

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

# 研究第一个仓库
repo_dict = repo_dicts[0]
# print(f'\nKeys: {len(repo_dict)}')
# for key in sorted (repo_dict.keys()):
#     print(key)

print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print(f"Name:{repo_dict['name']}")
    print(f"Owner:{repo_dict['owner']['login']}")
    print(f"Stars:{repo_dict['stargazers_count']}")
    print(f"Repository:{repo_dict['html_url']}")
    print(f"Created at:{repo_dict['created_at']}")
    print(f"Updated at:{repo_dict['updated_at']}")
    print(f"Description:{repo_dict['description']}")

