# 有一个列表 scores = [85, 92, 78, 90, 88]，请你写代码算出：
# 总分
# 平均分
# 最高分和最低分
# scores = [85, 92, 78, 90, 88]
# total = sum(scores)
#
# avg = total / len(scores)
#
# highest = max(scores)
#
# minest = min(scores)
#
# print(f'总分: {highest}')
# print(f'平均分：{avg}')
# print(f'最高分:{highest}')
# print(f'最低分:{minest}')
#
# import csv
# from pandas.core.computation.common import result_type_many
# from pyparsing import originalTextFor

#沿用上题的 scores，请用 for 循环遍历列表，只打印出 >= 80 分的成绩
# for score in scores:
#     if score >= 80:
#         print(score)
#


#创建一个字典，至少包含 3 种水果的名称和数量（比如苹果 5 个、香蕉 8 个、橘子 12 个），然后：
# 打印每种水果的库存
# 计算总共有多少个水果
# 添加一种新水果
# fruits = {'apple': 5, 'banana': 8, 'orange': 12}
# for fruit in fruits.items():
#     print(fruit)
#
# totals = sum(fruits.values())
# print(totals)
#
# fruits["葡萄"] = 20
# print(fruits)


# 写一个小程序：设定一个目标数字（比如 7），然后让用户输入猜测，根据猜测给出"大了"、"小了"或"猜对了"的反馈。
# target = 7
# max_attempts = 5
# print(f'请猜一个1~20之间的数字（最多{max_attempts}次机会）：')
# for attempt in range(1, max_attempts + 1):
#     guess = input(f'第{attempt}次猜测:')
#
#     # 处理输入非数字的情况
#     if not guess.isdigit():
#         print('请输入一个有效数字')
#         continue
#
#     guess = int(guess)
#
#     if guess > target:
#         print("你猜大了")
#     elif guess < target:
#         print("你猜小了")
#     else:
#         print(f"恭喜你猜对了,答案就是{target},你一共用了{attempt}次")
#         break
#
# else:
#     print(f'机会用完了，你没有猜中，答案是{target}')

# 写一个函数 describe_list(lst)，它接收一个数字列表，返回一段话，格式为：
# "列表有 X 个数，总和为 Y，平均值为 Z"
# 然后传入 [1, 2, 3, 4, 5] 测试一下。
# def describe_list(lst):
#     count = len(lst)
#     total = sum(lst)
#     average = total / count
#     return f'列表有{count}个数，总数为{total}，平均值为{average:.1f}'
#
# result = describe_list([1, 2, 3, 4, 5])
# print(result)

# 1.数据清洗  NONE判断，列表推导式【x for x in 。。。 if 。。。】
# raw_data = [1, 2, 3, 4, 5, None, -5, 2.8, -0.5, None]
# cleaned = []
# for x in raw_data:
#     if x is not None:
#         cleaned.append(x)
# print(f'清理前: {raw_data}')
# print(f'清理后: {cleaned}')
#
# cleaned2 = [x for x in cleaned if x is not None]
# print(f'推导式版：: {cleaned2}')


# 单词计数器，运用 .lower() .split() 字典统计模式
# 给定一段英文句子，统计每个单词出现的次数（不区分大小写）

# sentence = 'Python is great python is fun and Python is powerful'
#
# words = sentence.lower().split()   # 转小写 + 按空格分割
# word_count = {}
# for word in words:
#     if word not in word_count:
#         word_count[word] = 1
#     else:
#         word_count[word] += 1
#
# # 打印结果（按出现次数从高到低排列）
# for word, count in word_count.items():
#     print(f'{word}: {count} times')


# 简易记事本  文件读写 open（）/with/write()/read()
# todos = ['买牛奶','学python','跑步30分钟','回复邮件']
# filename = 'todos.txt'
#
# # 写入文件
# with open (filename,'w',encoding='utf-8') as file:
#     for i,task in enumerate(todos,start=1):
#         file.write(f'{i}. {task}\n')
# print(f'已写入{len(todos)}条件办到{filename}')
#
# # 读取文件
# with open (filename,'r',encoding='utf-8') as file:
#     print(f'\n---{filename}内容---')
#     for line in file:
#         print(f'{line.strip()}')


# 简易计算器 函数封装、边界情况处理（除以零、非法运算符）
# import math
#
#
# SUPPORTED_OPERATORS = ('+', '-', '*', '/', '//', '%', '**')
# OPERATOR_ALIASES = {'x': '*', '×': '*', '÷': '/'}
#
#
# def format_number(number):
#     """让整数结果不显示多余的 .0，并限制浮点数的显示长度。"""
#     if isinstance(number, float):
#         if number.is_integer():
#             return str(int(number))
#         return f'{number:.12g}'
#     return str(number)
#
#
# def simple_calculate(a, op, b):
#     """计算两个数字，并以易读的字符串返回结果或错误信息。"""
#     if isinstance(a, bool) or isinstance(b, bool):
#         return '错误：参与计算的内容必须是数字。'
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#         return '错误：参与计算的内容必须是数字。'
#     if (isinstance(a, float) and not math.isfinite(a)) or (
#             isinstance(b, float) and not math.isfinite(b)):
#         return '错误：请输入有限的数字。'
#     if not isinstance(op, str):
#         return '错误：运算符必须是字符串。'
#
#     op = OPERATOR_ALIASES.get(op.strip().lower(), op.strip())
#     if op not in SUPPORTED_OPERATORS:
#         operators = ' '.join(SUPPORTED_OPERATORS)
#         return f"错误：不支持运算符“{op}”，请使用 {operators}。"
#     if op in ('/', '//', '%') and b == 0:
#         return '错误：除数不能为 0。'
#     if op == '**' and abs(b) > 10000:
#         return '错误：指数过大，无法安全计算。'
#
#     try:
#         if op == '+':
#             result = a + b
#         elif op == '-':
#             result = a - b
#         elif op == '*':
#             result = a * b
#         elif op == '/':
#             result = a / b
#         elif op == '//':
#             result = a // b
#         elif op == '%':
#             result = a % b
#         else:
#             result = a ** b
#     except (ArithmeticError, ValueError):
#         return '错误：数值超出可计算范围。'
#
#     if isinstance(result, complex):
#         return '错误：当前计算器不支持复数结果。'
#     if isinstance(result, float) and not math.isfinite(result):
#         return '错误：计算结果超出有效范围。'
#
#     return f'{format_number(a)} {op} {format_number(b)} = {format_number(result)}'
#
#
# def read_number(prompt):
#     """反复读取数字；用户输入 q 时返回 None。"""
#     while True:
#         value = input(prompt).strip()
#         if value.lower() == 'q':
#             return None
#         try:
#             number = float(value)
#             if not math.isfinite(number):
#                 raise ValueError
#             return number
#         except ValueError:
#             print('输入无效，请输入数字（例如 12、-3.5），或输入 q 退出。')
#
#
# def run_calculator():
#     """运行可连续计算的命令行计算器。"""
#     operators = ' '.join(SUPPORTED_OPERATORS)
#     print('简易计算器')
#     print(f'支持的运算符：{operators}（也可使用 x、×、÷）')
#     print('在任意输入位置输入 q 即可退出。')
#
#     while True:
#         first_number = read_number('\n请输入第一个数字：')
#         if first_number is None:
#             break
#
#         operator = input('请输入运算符：').strip()
#         if operator.lower() == 'q':
#             break
#
#         second_number = read_number('请输入第二个数字：')
#         if second_number is None:
#             break
#
#         print(simple_calculate(first_number, operator, second_number))
#
#     print('计算器已退出。')
#
#
# if __name__ == '__main__':
#     run_calculator()



# 学生成绩分析  嵌套字典、if/elif/else多级评级、趋势对比
# student = {'姓名':'小明', '成绩':[88, 92, 76, 95, 83]}
# scores = student['成绩']
#
# # 基本统计
# avg = sum(scores)/len(scores)
# print(f'{student['姓名']}的成绩：{scores}')
# print(f'平均分：{avg:.1f}')
# print(f'最高分：{max(scores)}')
# print(f'最低分：{min(scores)}')
# print(f'考试次数:{len(scores)}')
#
# # 评级
# if avg >= 90:
#     grade = 'A'
# elif avg >= 80:
#     grade = 'B'
# elif avg >= 70:
#     grade = 'C'
# elif avg >= 60:
#     grade = 'D'
# else:
#     grade = 'F'
# print(f'评级：{grade}')
#
# first = scores[0]
# last = scores[-1]
# change = last - first
# if change >= 0:
#     trend = f'进步了{change}分'
# elif change < 0:
#     trend = f'退步了{abs(change)}分'
# else:
#     trend = '持平'
# print(f'趋势(首次{first} 到 末次{last}):{trend}')




# 订单分析 dict.get(name, o)安全取值、max(dict, key=...)按值找键
# 给定一组订单（用列表模拟csv数据），做基础统计
# orders = [
#     {"日期": "2026-07-01", "商品": "鼠标", "数量": 3, "单价": 299},
#     {"日期": "2026-07-01", "商品": "键盘", "数量": 1, "单价": 299},
#     {"日期": "2026-07-02", "商品": "鼠标", "数量": 5, "单价": 89},
#     {"日期": "2026-07-02", "商品": "显示器", "数量": 2, "单价": 1299},
#     {"日期": "2026-07-03", "商品": "键盘", "数量": 2, "单价": 299},
#     {"日期": "2026-07-03", "商品": "鼠标", "数量": 1, "单价": 89},
# ]
#
# # # 1.总销售额
# total_sales = sum(o["数量"] * o["单价"] for o in orders)
# print(f"总销量：cny{total_sales}")
#
# # # 2.总订单数
# print(f"订单数:{len(orders)}")
# #
# # # 3.每个商品的销售总量
# item_qty = {}
# for o in orders:
#     name = o["商品"]
#     item_qty[name] = item_qty.get(name, 0) + o["数量"]
# print(f"各商品销量：{item_qty}")
#
# # # 4.销售额最高的商品
# item_revenue = {}
# for o in orders:
#     name = o["商品"]
#     item_revenue[name] = item_revenue.get(name, 0) + o["数量"] * o["单价"]
# best_seller = max(item_revenue, key=item_revenue.get)
# print(f"销售额最高:{best_seller}(CNY{item_revenue[best_seller]})")
#
#
#
#
#
# # CSV读写  csv.DictWriter / csv.DictReader , 真正的表格文件操作
# # 把上面的数据写入 orders.csv 文件，再读回来验证
# import csv
#
# csv_file = "orders.csv"
# fieldnames = ["日期", "商品","数量", "单价"]
#
# # # 写入csv
# with open(csv_file, "w", newline="", encoding= "utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(orders)
# print(f"已写入{csv_file}")
#
# # # 读回 CSV
# with open(csv_file, "r", newline="", encoding= "utf-8") as f:
#     reader = csv.DictReader(f)
#     read_back = list(reader)
#     print(f"读回{len(read_back)}条记录")
#     for row in read_back:
#         print(f"{row['日期']} | {row['商品']:4s} | {row['数量']}个 | CNY{row['单价']}")
#
#
#
# # 按日期汇总 字典分组聚合模式（数据分析核心操作之一）
# daily_total = {}
# for o in orders:
#     date = o["日期"]
#     amount = o["数量"] * o["单价"]
#     if date in daily_total:
#         daily_total[date] += amount
#     else:
#         daily_total[date] = amount
#
# # # 按日期排序后输出
# for date in sorted(daily_total.keys()):
#     print(f"{date}: CNY{daily_total[date]}")
#
#
#
#
#
#
# # 日期计算 datetime/timedelta,星期差、星期几
# from datetime import datetime, timedelta
#
# d1 = datetime(2026, 7, 1)
# d2 = datetime(2026, 10, 7)
#
# diff = (d2 - d1).days
# print(f"{d1.date()} 到 {d2.date()} 相差{diff}天")
#
# future = datetime.now() + timedelta(days=30)
# print(f"30天后是:{future.date()}")
#
# # 中英文星期映射
# weekdays_cn = ["一", "二", "三", "四", "五", "六", "日"]
# today = datetime.now()
# print(f"今天是星期{weekdays_cn[today.weekday()]}")




# 生成报告 sorted()带key = lambda 排序、拼接字符串写入文件
# 综合前四个任务，生成一份文字报告并保存为.txt
# report_lines = []
# report_lines.append("=" * 30)
# report_lines.append("    销售数据分析报告")
# report_lines.append("=" * 30)
# report_lines.append(f"报告日期: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
# report_lines.append("")
# report_lines.append(f"1. 总销售额: CNY {total_sales}")
# report_lines.append(f"2. 订单总数: {len(orders)}")
# report_lines.append("")
# report_lines.append("3. 各商品销量:")
# for name, qty in item_qty.items():
#     report_lines.append(f"   - {name}: {qty} 个")
# report_lines.append("")
# report_lines.append("4. 各商品销售额:")
# for name, rev in sorted(item_revenue.items(), key=lambda x: x[1], reverse=True):
#     report_lines.append(f"   - {name}: CNY {rev}")
# report_lines.append("")
# report_lines.append("5. 每日销售额:")
# for date in sorted(daily_total.keys()):
#     report_lines.append(f"   - {date}: CNY {daily_total[date]}")
# report_lines.append("")
# report_lines.append(f"6. 销售额冠军: {best_seller} (CNY {item_revenue[best_seller]})")
# report_lines.append("=" * 30)
#
# report = "\n".join(report_lines)
# print(report)
#
# # 写入文件
# with open("报告.txt", "w", encoding="utf-8") as f:
#     f.write(report)
# print("\n报告已保存到 报告.txt")





# 写一个计算机订单函数。
# 场景：用户下单买了好几样菜，需要算总价
# 要求：
# 写函数 calc_order_total(items)，参数是一个列表，每个元素是字典 {"name": "有机菠菜", "price": 6.9, "qty": 2}
# 支持满减：满 99 减 10，满 199 减 30
# 返回最终应付金额（保留两位小数）

# def calc_order_total(items):
#     """计算订单总价，支持满减"""
#     # 1.计算原件总和
#     original = sum(item["price"] * item["qty"] for item in items)
#
#     # 2.满减逻辑，从高到低判断
#     if original >=199:
#         discount = 30
#     elif original >=99:
#         discount = 10
#     else:
#         discount = 0
#
#     # 3.计算最终金额
#     total = original - discount
#     return round(total,2)
#
# # 测试
# if __name__ == "__main__":
#     items = [
#         {"name": "有机蔬菜", "price": 6.9, "qty": 3},
#         {"name": "挪威三文鱼", "price": 89.0, "qty": 1},
#         {"name": "土鸡蛋", "price": 39.9, "qty": 1},
#     ]
#     result= calc_order_total(items)
#     print(f"应付金额：￥{result:.2f}")   # 应付金额：￥139
#
#     # 边界测试：刚好满99
#     items2 = [{"name":"A","price":99.0,"qty":1}]
#     print(f"应付金额：￥{calc_order_total(items2):.2f}")  # 89.00
#
#     # 边界测试：不满99
#     items3 = [{"name":"B","price":50.0,"qty":1}]
#     print(f"应付金额{calc_order_total(items3):.2f}")    # 50.00





# 任务2：设计一个商品类
# 场景：管理前置仓里的商品库存
# 要求：
# 写类 Product，包含属性：id、name、price、stock
# 方法 sell(qty)：扣减库存，库存不足时抛出 ValueError("库存不足")
# 方法 restock(qty)：增加库存
# 方法 info()：返回格式化字符串，如 "[P001] 有机菠菜 - ¥6.90 (库存: 120)"
# 魔术方法 __str__ 调用 info()

# class Product:
#     """生鲜商品"""
#     def __init__(self,product_id: str, name: str, price: float, stock: int):
#         self.id = product_id
#         self.name = name
#         self.price = price
#         self.stock = stock
#
#     def sell(self,qty: int):
#         """卖出 qty 件，库存不足抛异常"""
#         if qty > self.stock:
#             raise ValueError(f"库存不足：{self.name} 剩余 {self.stock}, 需要{qty}")
#         self.stock -= qty
#
#     def restock(self,qty: int):
#         """补货 qty 件"""
#         self.stock += qty
#
#     def info(self) -> str:
#         """格式化商品信息"""
#         return f"{self.id}{self.name} - ￥{self.price:.2f}(库存：{self.stock})"
#
#     def __str__(self) -> str:
#         """print(p)时自动调用 info（）"""
#         return self.info()
#
# # 测试
# if __name__ == "__main__":
#     p = Product("P001", "有机蔬菜", 6.90, 120)     # [P001]有机蔬菜 - ￥6.90(库存：120)
#     print(p)
#     p.sell(30)      # 90
#     print(p.stock)
#     p.restock(50)   #140
#     print(p.stock)
#     try:
#         p.sell(200)     # 抛出 ValueError
#     except ValueError as e:
#         print(f"错误:{e}")    # 错误：库存不足，有机蔬菜 剩余 140，需要200





# 任务 3：用 async/await 并发请求多个接口
# 场景：小程序首页需要同时加载商品列表、促销活动、用户信息三个接口，串行太慢，用并发。
# 要求：
# 写异步函数 fetch_all()，并发请求 3 个 URL
# 用 asyncio.gather 并发执行
# 模拟网络延迟：每个请求 await asyncio.sleep(随机1~3秒)
# 打印每个请求的耗时，最后打印总耗时
# 总耗时应该接近最慢的那个请求（约 3 秒），而不是三个加起来（约 6 秒）

# import asyncio
# import time
# import random
#
# async def fetch(url: str, name: str) -> dict:
#     """模拟异步请求,随机延迟1~3秒"""
#     start = time.time()
#     delay = random.randint(1, 3)
#     await asyncio.sleep(delay)
#     elapsed = time.time() - start
#     print(f"[{name}{url}完成，耗时 {elapsed:.2f}s]")
#     return {"name": name, "data": f"response from {url}"}
#
# async def fetch_all():
#     """并发请求三个接口"""
#     urls = [
#         ("https://api.xianda.com/v1/products", "商品列表"),
#         ("https://api.xianda.com/v1/promotions", "促销活动"),
#         ("https://api.xianda.com/v1/user/profile", "用户信息")
#     ]
#
#     print("开始并发请求。。。")
#     start_total = time.time()
#
#     # 用 asyncio.gather 并发执行多个协程
#     results = await asyncio.gather(
#         *[fetch(url,name) for url, name in urls]
#     )
#
#     total_elapsed = time.time() - start_total
#     print(f"\n全部完成！总耗时{total_elapsed:.2f}s")
#     # 总耗时 ≈ 最慢的那个请求（~3s），而不是三个加起来(~6s)
#
#     print(f"\n返回结果：")
#     for r in results:
#         print(f"{r}")
#
# # 入口
# if __name__ == "__main__":
#     asyncio.run(fetch_all())
#


# 第三部分：REST API 调用
# 任务 6：GET 请求 + JSON 解析
# 场景：调用一个公开的测试 API 获取数据。
#
# 要求：
#
# 用 requests 库 GET 请求 https://jsonplaceholder.typicode.com/users
# 解析返回的 JSON，提取每个用户的 name、email、所在城市 address.city
# 打印成表格格式：

# import requests
#
# def fetch_users():
#     """GET请求获取用户列表，打印表格"""
#     url = "https://jsonplaceholder.typicode.com/users"
#
#     # 发 GET 请求
#     resp = requests.get(url)
#     resp.raise_for_status()     # 状态码不是 2xx 会抛异常
#
#     users = resp.json()     # 自动解析 JSON
#
#     # 打印表头
#     print(f"{"姓名":<16} {"城市"}")
#     print("-" * 16 + " " + "-" * 27 + " " + "-" * 10)
#
#     # 打印每一行
#     for user in users:
#         name = user["name"]
#         email = user["email"]
#         city = user["address"]["city"]
#         print(f"{name:<16} {email:<27} {city}")
#
#     print(f"\n共{len(users)} 个用户")
#
# if __name__ == "__main__":
#     fetch_users()



# 任务 7：POST 请求 + Auth Header
# 场景：模拟小程序提交订单到后端 API。
# 要求：
# 用 requests POST 请求 https://jsonplaceholder.typicode.com/posts
# 请求头带 Authorization: Bearer your-token-here
# 请求体（JSON）：

import requests

def submit_order():
    """POST请求提交订单，带Authorization header"""
    url = "https://jsonplaceholder.typicode.com/posts"

    # 请求头：Bearer Token 认证
    headers = {
        "Authorization":"Bearer your-token-here",
    }

    # 请求体(JSON)
    order_data = {
        "userId":1,
        "title":"生鲜订单-20260717",
        "body":"有机蔬菜×2，挪威三文鱼×1",
    }

    # 发POST 请求
    # json = 参数会自动设置Content-Type：application/json
    resp = requests.post(url, headers=headers, json=order_data)

    print(f"状态码：{resp.status_code}")

    # 从响应头获取Content-Type(大小写不敏感)
    content_type = resp.headers.get("Content-Type", "unknow")
    print(f"Content-Type:{content_type}")

    # 解析返回的JSON
    data = resp.json()
    print(f"新创建的资源ID：{data['id']}")

# if __name__ == "__main__":
#     submit_order()
#













































# 第四部分：YAML 与 JSON 读写
# 任务 8：读 JSON → 筛选 → 写 JSON
# 场景：前置仓要导出库存低于 100 的商品清单。
# 要求：
# 读取 data/products.json（已提供）
# 筛选出 stock < 100 的商品
# 输出到 data/low_stock.json

import json

def filter_low_stock():
    """读 products.json,筛选库存<100的商品，输出到 low_stock.json"""
    input_path = "data/products.json"
    output_path = "data/low_stock.json"

    # 读JSON
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    products = data["products"]     # 商品列表

    # 筛选库存不足的商品，只保留 id / name / stock
    low_stock = [
        {"id": p["id"], "name": p["name"], "stock": p["stock"]}
        for p in products
        if p["stock"] < 100
    ]

    # 写JSON（ensure_ascii = False 保证中文不转义围殴\uxxxx）
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(low_stock, f, ensure_ascii=False, indent=2)

    print(f"低库存商品(stock < 100):")
    for item in low_stock:
        print(f"{item['id']} {item['name']} - 库存:{item['stock']}")
    print(f"\n已写入{output_path}")

if __name__ == "__main__":
    filter_low_stock()