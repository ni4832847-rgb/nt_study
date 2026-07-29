import requests
import plotly.express as px

# 执行API调用并查看响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+stars:%3E10000&sort=stars&order=desc"

headers = {"Accept":"application/vnd.github.v3+json"}
proxies = {"http": "http://127.0.0.1:33210", "https": "http://127.0.0.1:33210"}
r = requests.get(url, headers=headers, proxies=proxies)
print(f"Status code: {r.status_code}")

# 处理结果
response_dict = r.json()
print(f"Complete results:{not response_dict['incomplete_results']}")

# 处理有关仓库的信息
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # 将仓库名转换为连接
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href={repo_url}>{repo_url}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # 创建悬停文本
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 可视化
title = "Most-Starred Python Projects on Github"
labels = {'x':'Repository','y':'Stars'}
fig = px.bar(x=repo_links, y=stars,  labels=labels, title=title , hover_name=hover_texts)

fig.update_layout(title_font_size=28,xaxis_title_font_size=20,yaxis_title_font_size=20)
# fig.update_traces(marker_color='Blue',marker_opacity=0.6)
fig.show()
