# 创建一个列表 nums = [10, 20, 30, 40, 50, 60, 70]，完成以下操作：
# 取出前 3 个元素
# 取出最后 2 个元素
# 取出索引 2 到 5 的元素
import avg
import params

# original = {"name": "张三", "age": 25, "city": "合肥"}
# original1 = {v:k for k, v in original.items()}
# print(original1)

# sentence = "the cat and the dog and the bird"
# words = sentence.split()
# freq = {}
# for w in words:
#     freq[w] = freq.get(w, 0) + 1
# print(freq)
#
#
# fib = [0, 1]
# while len(fib) < 15:
#     fib.append(fib[-1] + fib[-2])
# print(fib)




# cities = [
#     {"province": "安徽", "cities": ["合肥", "芜湖", "黄山"]},
#     {"province": "江苏", "cities": ["南京", "苏州"]},
#     {"province": "浙江", "cities": ["杭州", "宁波", "温州"]},
# ]
# all_cities = [city for prov in cities for city in prov["cities"]]
# print(all_cities)



# def sample(data, rate):
#     step = int(1/rate)
#     return data[::step]
# print(sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 0.3 ))





# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transposed = [[row[i] for row in matrix] for i in range(3)]
# print(transposed)




# import re
#
# def clean_text(text):
#     text = text.strip()
#     text = re.sub(r'[,.!?;:()\[\]]', ' ', text)
#     text = text.lower()
#     words = text.split()
#     return [w for w in words if len(w) >= 2]
#
# print(clean_text("Hello, World! This is a test. (Good luck!)"))






# students = [
#     {"name": "张伟", "score": 88},
#     {"name": "李娜", "score": 95},
#     {"name": "王强", "score": 45},
#     {"name": "赵敏", "score": 73},
#     {"name": "刘洋", "score": 62},
#     {"name": "陈杰", "score": 91},
#     {"name": "杨柳", "score": 58},
#     {"name": "孙浩", "score": 76},
#     {"name": "周舟", "score": 84},
#     {"name": "吴迪", "score": 39},
# ]
#
# def analyze_student(students):
#     scores = [s["score"] for s in students]
#     avg = sum(scores) / len(scores)
#
#     top = max(students, key = lambda s: s["score"])
#     bottom = min(students, key = lambda s: s["score"])
#
#     levels = {
#         "优秀(>=90)": len([s for s in students if s["score"] >= 90]),
#         "良好(>=80)": len([s for s in students if 80 <= s["score"] <= 90]),
#         "中等(>=70)": len([s for s in students if 70 <= s["score"] <= 80]),
#         "及格(>=60)": len([s for s in students if 60 <= s["score"] <= 70]),
#         "不及格(<60)": len([s for s in students if s["score"] < 60]),
#     }
#
#     return {
#         "平均分": round(avg, 1),
#         "最高分": top,
#         "最低分": bottom,
#         "分数段": levels,
#     }
#
# print(analyze_student(students))





# import json
#
# data = [
#     {"id": 1, "name": "张三", "email": "zhangsan@example.com", "active": True},
#     {"id": 2, "name": "李四", "email": "lisi@example.com", "active": False},
#     {"id": 3, "name": "王五", "email": "wangwu@example.com", "active": True},
#     {"id": 4, "name": "赵六", "email": "zhaoliu@example.com", "active": False},
#     {"id": 5, "name": "钱七", "email": "qianqi@example.com", "active": True},
#     {"id": 6, "name": "孙八", "email": "sunba@example.com", "active": True},
# ]
#
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)
# print("data.json 已生成")
#
# with open("data.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#
# users = [
#     {"name": d["name"], "email": d["email"]}
#     for d in data if d["active"]
# ]
#
# with open("users.json", "w", encoding="utf-8") as f:
#     json.dump(users, f, ensure_ascii=False, indent=2)
#
# print(f"已保存 {len(users)} 个活跃用户")






# KEYWORDS = {
#     "运动":["篮球", "足球", "跑步", "游泳", "健身", "比赛"],
#     "科技":["AI", "编程", "python", "数据", "算法", "代码"],
#     "美食":["美食", "烹饪", "菜谱", "火锅", "甜品", "烧烤"],
# }
#
# def classify(text):
#     scores = {}
#     for category, words in KEYWORDS.items():
#         scores[category] = sum(1 for w in words if w in text)
#
#     max_score = max(scores.values())
#     if max_score == 0:
#         return "其他"
#
#     winners = [cat for cat,s in scores.items() if s == max_score]
#     return winners[0] if len(winners) == 1 else "其他"
#
# text1 = "我喜欢打篮球和跑步，偶尔也会看足球比赛"
# text2 = "用Python编写AI算法，分析数据并优化代码"
# text3 = "火锅和烧烤是我最爱的美食，偶尔也研究菜谱"
# text4 = "我打篮球的同时也在学Python编程"  # 应该归为其他（平局）
#
# print(classify(text1))  # 运动
# print(classify(text2))  # 科技
# print(classify(text3))  # 美食
# print(classify(text4))  # 其他







# import requests
#
# # 最基本的 GET 请求
# response = requests.get("https://httpbin.org/get")
#
# print("状态码",response.status_code)       # 200 = 成功
# print("json 数据",response.json())         # 解析成 python 字典
# print("响应头",dict(response.headers))     # 服务器返回的元信息




import requests



#
# URL = "https://official-joke-api.appspot.com/random_joke"
# response = requests.get(URL)
# data = response.json()
# print(f"笑话:{data['setup']}")
# print(f"包袱:{data['punchline']}")







# URL = "https://randomuser.me/api/"
# params= {"results":5,"nat":"CN"}
# response = requests.get(url = URL, params = params)
# data = response.json()
#
# users = [
#     {
#         "name":f"{u['name']['first']}{u['name']['last']}",
#         "email":u["email"],
#         "city":u['location']['city']
#     }for u in data["results"]
# ]
# import json
# print(json.dumps(users,ensure_ascii=False, indent=2))



# URL = "https://api.open-meteo.com/v1/forecast"
# def get_weather(city, lat, lon):
#     params = {
#         "latitude": lat,
#         "longitude": lon,
#         "current_weather": True
#     }
#     response = requests.get(URL, params=params)
#     w = response.json()["current_weather"]
#     return {
#         "city": city,
#         "temperature": w['temperature'],
#         "windspeed": w['windspeed'],
#         "weathercode": w['weathercode'],
#     }
#
# for city, lat, lon in [("北京", 39.91, 116.49),("上海", 31.23,121.47), ("合肥", 31.82, 117.23),("深圳", 22.54, 114.06)]:
#     print(get_weather(city, lat, lon))







# URL = "https://jsonplaceholder.typicode.com/posts"
# post_data = {
#     "title": "python API 调用入门",
#     "body":"这是我第一篇通过 API 提交的文章",
#     "userId": 1
# }
#
# response = requests.post(url=URL, json=post_data)
# print(response.json())
# # 服务器会返回带 id = 101 的数据（JSONPlaceholder 不会真的储存）




# import json
#
# URL = "https://www.boredapi.com/api/activity"
# def get_activity(activity_type = None):
#     params = {}
#     if activity_type:
#         params['type'] = activity_type
#     response = requests.get(URL, params = params)
#     return response.json()
#
# activity = get_activity("education")
#
# if activity["participants"]:
#     print(f"多人活动{activity['participants']}人):{activity['activity']}")
#     print("重新活动单人活动。。。。")
#     activity = get_activity()   #   不限类型
#     while activity['participants'] > 1:
#         activity = get_activity()
#
# print(json.dumps(activity, ensure_ascii=False, indent=2))



# 进阶：异常处理（真实项目中必须写）
# 网络请求随时可能失败——超时、断网、服务器挂了。任何生产代码都要包 try/exce
def safe_get(url, params=None, timeout=5):
    """安全的 GET 请求，带异常处理和超时"""
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()  # 非 200 就抛异常
        return response.json()
    except requests.exceptions.Timeout:
        print(f"请求超时（超过 {timeout} 秒）")
        return None
    except requests.exceptions.ConnectionError:
        print("网络连接失败")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误: {e}")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None

# 测试
data = safe_get("https://official-joke-api.appspot.com/random_joke")
if data:
    print(f"Setup: {data['setup']}")
    print(f"Punchline: {data['punchline']}")











































