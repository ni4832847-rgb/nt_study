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

# import requests
#
# def submit_order():
#     """POST请求提交订单，带Authorization header"""
#     url = "https://jsonplaceholder.typicode.com/posts"
#
#     # 请求头：Bearer Token 认证
#     headers = {
#         "Authorization":"Bearer your-token-here",
#     }
#
#     # 请求体(JSON)
#     order_data = {
#         "userId":1,
#         "title":"生鲜订单-20260717",
#         "body":"有机蔬菜×2，挪威三文鱼×1",
#     }
#
#     # 发POST 请求
#     # json = 参数会自动设置Content-Type：application/json
#     resp = requests.post(url, headers=headers, json=order_data)
#
#     print(f"状态码：{resp.status_code}")
#
#     # 从响应头获取Content-Type(大小写不敏感)
#     content_type = resp.headers.get("Content-Type", "unknow")
#     print(f"Content-Type:{content_type}")
#
#     # 解析返回的JSON
#     data = resp.json()
#     print(f"新创建的资源ID：{data['id']}")
#
# if __name__ == "__main__":
#     submit_order()









# 第四部分：YAML 与 JSON 读写
# 任务 8：读 JSON → 筛选 → 写 JSON
# 场景：前置仓要导出库存低于 100 的商品清单。
# 要求：
# 读取 data/products.json（已提供）
# 筛选出 stock < 100 的商品
# 输出到 data/low_stock.json

# import json
# from pathlib import Path
#
# def filter_low_stock():
#     """读 products.json,筛选库存<100的商品，输出到 low_stock.json"""
#     data_dir = Path(__file__).resolve().parent / "data"
#     input_path = data_dir / "products.json"
#     output_path = data_dir / "low_stock.json"
#
#     # 读JSON
#     with open(input_path, "r", encoding="utf-8") as f:
#         data = json.load(f)
#
#     products = data["products"]     # 商品列表
#
#     # 筛选库存不足的商品，只保留 id / name / stock
#     low_stock = [
#         {"id": p["id"], "name": p["name"], "stock": p["stock"]}
#         for p in products
#         if p["stock"] < 100
#     ]
#
#     # 写JSON（ensure_ascii = False 保证中文不转义围殴\uxxxx）
#     # with open(output_path, "w", encoding="utf-8") as f:
#     #     json.dump(low_stock, f, ensure_ascii=False, indent=2)
#
#     print(f"低库存商品(stock < 100):")
#     for item in low_stock:
#         print(f"{item['id']} {item['name']} - 库存:{item['stock']}")
#     print(f"\n已写入 {output_path}")
#
# if __name__ == "__main__":
#     filter_low_stock()







# 任务 9：读 YAML 配置 → 改值 → 写回
# 场景：运营要调整免配送费门槛从 59 元降到 49 元，同时加一个满 299 减 50 的活动。
# 要求：
# 读取 data/config.yaml（已提供）
# 修改 free_delivery_threshold 为 49.0
# 在 tiered_discount 列表末尾追加 {"threshold": 299, "reduce": 50}
# 写回 data/config_updated.yaml（不要覆盖原文件）
# 打印修改前后的免配送费门槛对比

# from pathlib import Path
#
# import yaml
#
# def update_config():
#     """读 YAML 配置，修改免配送费门槛 + 满减活动，写回新文件"""
#     data_dir = Path(__file__).resolve().parent / "data"
#     input_path = data_dir / "config.yaml"
#     output_path = data_dir / "config_updated.yaml"
#
#     # 读YAML
#     with open(input_path, "r", encoding="utf-8") as f:
#         config = yaml.safe_load(f)
#
#     old_threshold = config["delivery"]["free_delivery_threshold"]
#
#     # 修改免配送费门槛
#     config["delivery"]["free_delivery_threshold"] = 49.0
#
#     # 在满减活动中追加一项
#     config["promotion"]["tiered_discount"].append(
#         {"threshold": 299, "reduce": 50}
#     )
#
#     new_threshold = config["delivery"]["free_delivery_threshold"]
#
#     # 对比
#     print(f"免配送费门槛：￥{old_threshold} -> ￥{new_threshold}")
#
#     # 查看递减
#     discounts = config["promotion"]["tiered_discount"]
#     print(f"满减活动({len(discounts)}档):")
#     for d in discounts:
#         print(f"满￥{d['threshold']} 减 ￥{d['reduce']}")
#
#     # 写 YAML （不覆盖原文件）
#     with open(output_path, "w", encoding="utf-8") as f:
#         yaml.safe_dump(
#             config,
#             f,
#             allow_unicode=True,
#             default_flow_style=False,
#             sort_keys=False,
#         )
#
#     print(f"\n已写入 {output_path}")
#
# if __name__ == "__main__":
#     update_config()







# 第五部分：综合实战
# 任务 10：把以上全部串起来
# 场景：写一个小脚本 inventory_report.py，完成以下全部流程：
# 读 YAML 配置：加载 data/config.yaml，获取 api.base_url 和 api.timeout
# 读 JSON 数据：加载 data/products.json，获取商品列表
# 用类管理：把每个商品实例化为 Product 对象（复用任务 2 的类）
# 用函数计算：对每个商品按 price * 1.05（加 5% 损耗）算实际成本，用函数实现
# 并发模拟：用 async/await 模拟并发向 3 个前置仓查询库存（每个 sleep 1~2 秒）
# 输出报告：把结果写入 data/report.json，格式
# Git 提交：完成后 git add + git commit -m "add inventory report script"






# 任务 11：写两个 Python 装饰器
# 场景：线上排查问题时，需要知道某些函数执行了多久；调用外部接口时，网络抖动需要自动重试。
# 要求：
# 11-1：计时装饰器 @timer
# 装饰任意函数，打印函数名和执行耗时（精确到毫秒）
# 支持带参数和不带参数的函数
# 11-2：重试装饰器 @retry(max_times=3, delay=1)
# 函数抛出异常时自动重试，最多 max_times 次
# 每次重试间隔 delay 秒
# 用光重试次数后把原始异常抛出去


# import time
# import functools
#
# # 计时装饰器
# def timer(func):
#     """打印函数执行耗时"""
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         elapsed = (time.time() - start) * 1000      # 转毫秒
#         print(f"{timer} {func.__name__}: {elapsed:.2f} ms")
#         return result
#     return wrapper
#
# # 重试装饰器
# def retry(max_times = 3,delay = 1):
#     """带参数装饰器，函数抛异常时自动重试"""
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             last_exc = None
#             for attempt in range(1,max_times + 1):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     last_exc = e
#                     if attempt < max_times:
#                         print(f"{retry}{func.__name__}第 {attempt}/{max_times}次失败"f"({e}),{delay}秒后重试。。。")
#                         time.sleep(delay)
#             # 重试耗尽，抛出最后一次异常
#             raise last_exc
#         return wrapper
#     return decorator
#
# # 测试
# import requests
#
# @retry(max_times=3,delay=2)
# def fetch_price(product_id):
#     resp = requests.get(f"https://httpbin.org/status/500")  # 故意请求一次
#     resp.raise_for_status()
#     return resp.json()
#
# @timer
# def heavy_calculation(n):
#     return sum(i * i for i in range(n))
#
# if __name__ == '__main__':
#     print("===测试timer===")
#     result = heavy_calculation(10_000_000)
#
#     print("\n=== 测试 retry ===")
#     try:
#         fetch_price("P001")
#     except Exception as e:
#         print(f"[main]最终失败:{e}")









# 任务 12：上下文管理器
# 场景：连接数据库/打开文件后要确保关闭，不管中间是否发生异常。
# 要求：
# 12-1：文件操作上下文管理器（用 @contextmanager）
# 写 @contextmanager 生成器函数 safe_open(filepath, mode)
# 进入时打开文件，退出时自动关闭
# 支持自动创建目录（如果中间路径不存在）
# 对比普通 open 和 safe_open 的写法
# 12-2：数据库连接模拟（用 __enter__ / __exit__）
# 写类 Database，带 connect()、close()、execute(sql) 方法
# 实现 __enter__（连接数据库）和 __exit__（断开连接）
# execute 只是打印 SQL，不做真实操作
# 在 __exit__ 中即使 execute 抛异常也保证 close

# import os
# from contextlib import contextmanager
#
# # 12.1 用 @contextmanager 实现
# @contextmanager
# def safe_open(filepath, mode):
#     """安全打开文件：会自动创建目录（如果不存在）"""
#     dir_path = os.path.dirname(filepath)
#     if dir_path and not os.path.exists(dir_path):
#         os.makedirs(dir_path,exist_ok=True)
#         print(f"[safe_open] 创建目录:{dir_path}")
#
#         # 进入上下文:打开文件
#         f = open(filepath, mode, encoding="utf-8")
#         print(f"[safe_open] 打开文件:{filepath}")
#
#         try:
#             yield f     # 把文件对象交给with块
#         finally:
#             f.close()   # 退出上下文：无论如何都会关闭
#             print(f"[safe_open] 关闭文件:{filepath}")
#
# # 12.2:用__enter__/__exit__ 实现
# class Database:
#     """模拟数据库连接"""
#
#     def __init__(self,connection_string):
#         self.connection_string = connection_string
#         self.connected = False
#
#     def __enter__(self):
#         """进入 with 块时调用"""
#         self.connect()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """返回 with 块时调用（即使有异常也会走这里）"""
#         self.close()
#         # 返回 False 表示不吞掉异常（异常继续向上传播）
#         return False
#
#     def connect(self):
#         print(f"[Database] 连接:{self.connection_string}")
#         self.connected = True
#
#     def close(self):
#         print(f"[Database] 连接:{self.connection_string}")
#         self.connected = False
#
#     def execute(self,sql):
#         if not self.connected:
#             raise RuntimeError("数据库未连接")
#         print(f"[Database] 执行 SQL:{sql}")
#         return f"结果：{sql}"
#
# # 测试
# if __name__ == "__main__":
#     # 测试 safe_open
#     print("===safe_open===")
#     with safe_open("data/logs/app.log",'w') as f:
#         f.write("服务启动成功\n")
#
#     # 对比：传统写法需要手动try/finally
#     print("\n传统写法（繁琐）:")
#     f = open("data/logs/app.log","w")
#     try:
#         f.write("旧方式\n")
#     finally:
#         f.close()
#
#
#     # 测试Database
#     print("\n===Database===")
#     with Database("mysql://localhost:3306/fresh") as db:
#         db.execute("select * from fresh")
#         db.execute("update products set stock = 100 where id='P001'")
#
#     # 测试异常安全
#     print("\n===异常安全测试===")
#     try:
#         with Database("mysql://localhost:3306/fresh") as db:
#             db.execute("select * from products")
#             raise ValueError("模拟业务异常")      # 即使抛异常，也会 close
#     except ValueError:
#         print("捕获异常，但数据库已经安全断开了")
#






# 任务 13：完善的异常处理
# 场景：调用第三方价格查询 API，可能遇到网络超时、返回异常格式、token 过期等情况，需要分类处理。
# 要求：
# 写函数 get_product_price(product_id)，调用 https://httpbin.org/delay/{n} 模拟（n 随机 0~5）
# 正确处理以下异常层级：
# requests.Timeout → 打印"请求超时，请稍后重试"
# requests.ConnectionError → 打印"网络连接失败，检查网络"
# requests.HTTPError → 根据状态码打印不同信息（401 token过期、404 商品不存在、500 服务器错误）
# json.JSONDecodeError → 打印"接口返回格式异常"
# Exception → 兜底
# 用 else 和 finally 补充逻辑：
# else：成功的分支，打印价格
# finally：无论成败都打印"--- 查询结束 ---"
# 自定义异常类 APIError，继承 Exception，包含 status_code 和 message 属性

# import json
# import random
# import requests
#
# # 自定义异常
# class APIError(Exception):
#     """自定义 API 异常，携带状态码"""
#     def __init__(self, status_code: int, message: str):
#         self.status_code = status_code
#         self.message = message
#         super().__init__(f"[HTTP{status_code}]{message}")
#
# # 主逻辑
# def get_product_price(product_id:str) -> dict | None:
#     """
#     查询商品价格，完善的异常处理。
#     返回价格信息，失败时返回None。
#     """
#     # 随机模拟： 0=成功 1=404 2=500 3=超时 4=连接失败 5=返回乱码
#     scenario = random.randint(0, 5)
#     delay = scenario if scenario <= 2 else 3    # 后三种不走 httpbin delay
#
#     timeout = 5
#
#     if scenario == 0:
#         url = f"https://httpbin.org/delay/{delay}"
#     elif scenario == 1:
#         url = "https://httpbin.org/status/404"
#     elif scenario == 2:
#         url = "https://httpbin.org/status/500"
#     elif scenario == 3:
#         url = "https://httpbin.org/delay/30"
#         timeout = 3
#     elif scenario == 4:
#         url = "https://192.0.2.0/nowhere"
#     else:
#         url = "https://httpbin.org/html"
#
#     try:
#         # 发请求
#         print(f"本次 timeout：{timeout} 秒")
#         resp = requests.get(url, timeout=timeout)
#         resp.raise_for_status()     # 4xx/5xx 自动转 HTTPError
#
#         # 解析 JSON
#         data = resp.json()
#
#     except requests.Timeout:
#         print("请求超时，请稍后重试")
#         return None
#     except requests.ConnectionError:
#         print("网络连接失败，检查网络")
#         return None
#
#     except requests.HTTPError as e:
#         status = e.response.status_code
#         if status == 401:
#             print(f"Token 过期(401),请重新登录")
#         elif status == 403:
#             print(f"无访问权限(403)")
#         elif status == 404:
#             print(f"商品{product_id} 不存在(404)")
#         elif 500 <= status < 600:
#             print(f"服务器错误({status}),请稍后重试")
#         else:
#             print(f"HTTP 错误（{status}）")
#         return None
#
#     except json.JSONDecodeError:
#         print("接口返回格式异常，无法解析JSON")
#         return None
#
#     except Exception as e:
#         print(f"未知错误：{e}")
#         return None
#
#     else:
#         # try 块没有异常才会执行这里
#         print(f"商品{product_id}价格查询成功")
#         return data
#
#     finally:
#         # 无论如何都会执行
#         print("---查询结束---")
#
# # 测试
# if __name__ == "__main__":
#     for _ in range(5):
#         print()
#         get_product_price("P001")







# 任务 14：生成器与迭代器
# 场景：双十一当天订单量暴增，一次性把所有订单加载到内存会 OOM。用生成器做懒加载。
# 19-1：生成器函数 order_stream()
# 写生成器函数，用 yield 逐条产出模拟订单
# 每调用一次 next() 返回一条订单字典
# 用 random 随机生成：{"order_id": "ORD001", "amount": 89.5, "items": 3}
# 产出 10 条后自动结束（不提前生成 10 条放在内存里）
# 19-2：生成器表达式
# 用生成器表达式 (...) 筛选出 amount > 100 的订单
# 对比：如果用列表推导 [...]，内存差异在哪
# 19-3：自定义迭代器类 ProductPage
# 实现 __iter__ 和 __next__，模拟分页加载商品
# 构造函数传入 products 列表和 page_size
# 每次迭代返回一页商品（切片），取完自动 StopIteration

# import random
# from typing import Generator,Iterator
#
# # 19.1 生成器函数
# def order_stream(n: int = 10) -> Generator[dict, None, None]:
#     """用yield逐条产生订单，不会一次性加载全部"""
#     for i in range(1,n+1):
#         yield {
#             "order_id": f"ORD{i:04d}",
#             "amount":round(random.uniform(20, 300),2),
#             "items": random.randint(1,8),
#             "city": random.choice(["合肥", "芜湖", "蚌埠", "安庆"]),
#         }
#
# # 19.2:生成器表达式 vs 列表推导
# print("===生成器表达式===")
# # 生成器表达式：不立即计算，迭代时才逐个产出
# large_orders = (o for o in order_stream(10000) if o["amount"] > 1000)
# print(f"类型:{type(large_orders)}")       # <class 'generator'>
# print(f"前5条大额订单：")
# for i,order in enumerate(large_orders):
#     print(f"{order['order_id']}: ￥{order['amount']:.2f}")
#     if i >= 4:
#         break
#
# # 对比：列表推导会立刻生成 10000 条放进内存
# # large_orders_list = [o for o in order_stream(10000) if o["amount"] > 100]
# # 内存占用 ≈ 10000 * 每个字典大小
#
# # 19.3：自定义迭代器类
# class ProductPage:
#     """分页迭代器：每返回一页首页"""
#
#     def __init__(self, products: list, page_size: int =3):
#         self.products = products
#         self.page_size = page_size
#         self.cursor = 0     # 当前页起始索引
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.cursor >= len(self.products):
#             raise StopIteration
#         start = self.cursor
#         end = start + self.page_size
#         self.cursor = end
#         return self.products[start:end]
#
# # 测试
# if __name__ == "__main__":
#     # 测试生成器函数
#     print("==== order_stream 前三条====")
#     stream = order_stream(5)
#     print(next(stream))
#     print(next(stream))
#     print(f"剩余：{list(stream)}")     # 取完余额 StopIteration, list() 自动处理
#
#     # 测试迭代器
#     print("\n==== ProductPage分页 ====")
#     sample_products = [
#         {"id":f"P{i}","name":f"商品{i}","price": i * 10}
#         for i in range(1,11)
#     ]
#     pager = ProductPage(sample_products, page_size=3)
#     for page_num, page in enumerate(pager,1):
#         print(f"第{page_num}页:{[p['id'] for p in page]}")








# 任务 20：高阶数据结构
# 场景：运营要做月度销售分析——按品类汇总销售额、统计各商品出现次数、用命名元组让代码更可读。
# 20-1：defaultdict 按品类汇总
# 给定订单列表（每个订单有 category 和 amount）
# 用 collections.defaultdict(float) 不写 if key in dict 的判断
# 输出各品类总销售额
# 20-2：Counter 统计畅销品
# 给定订单列表，每单有 product_name
# 用 Counter 统计每个商品被购买的次数
# 输出 Top 3，用 most_common(3)
# 20-3：namedtuple 让订单可读
# 用 namedtuple 定义 Order = namedtuple("Order", ["id", "amount", "category", "city"])
# 把字典列表转成 namedtuple 列表
# 通过 .amount（而非 ["amount"]）访问字段
# 对比字典和 namedtuple 的内存占用（sys.getsizeof）

from collections import defaultdict, Counter, namedtuple
import random
import sys

# 模拟数据
CATEGORIES = ["蔬菜", "海鲜", "肉类", "预制菜", "粮油"]
PRODUCTS = ["有机蔬菜", "挪威三文鱼", "土鸡蛋", "酸菜鱼", "五常大米", "宁夏滩羊肉", "手撕牛肉干", "鲜牛奶"]

random.seed(42)
orders = [
    {
        "id": f"ORD{i:04d}",
        "amount": round(random.uniform(1, 100), 2),
        "category": random.choice(CATEGORIES),
        "product_name":round.choice(PRODUCTS),
        "city":random.choice(["合肥","芜湖","蚌埠"]),
    }
    for i in range(1,51)
]

# 20.1: defaultdict 按品类汇总
print("====各品类销售额====")
sales_by_cat = defaultdict(float)   # 默认值 0，0，不用写 if key not in dict

for order in orders:
    sales_by_cat[order["category"]] += order["amount"]

# 普通 dict 需要这样写：
# sales_by_cat = {}
# for order in orders:
#       cat = order["category"]
#       if cat no in sales_by_cat:
#           sales_by_cat[cat] = 0
#       sales_by_cat[cat] += order["amount"]

for cat, total in sorted(sales_by_cat.items(),key=lambda x: x[1], reverse=True):
    print(f"{cat}: ￥{total:.2f}")

# 20.2:Counter 统计畅销品
print("\n==== 商品购买次数 Top3 ====")
product_counter = Counter(order["product_name"] for order in orders)

for product, count in product_counter.most_common(3):
    print(f"{product}: {count}次")

# Counter 还支持数学运算
print(f"\n 总订单数：{product_counter.total()}")
# 两个Counter 可以相加、相减

# 20.3：namedtuple
# 定义命名元组
Order = namedtuple("Order", ["order_id", "amount", "category", "product_name"])

# 字典 -> namedtuple
nt_orders = [
    Order(o["id"],o["amount"], o["category"], o["city"])
]

# 访问方式对比
a_dict = orders[0]
a_nt = nt_orders[0]

print("\n====namedtuple vs dict====")
print(f"dict访问:{a_dict['amount']}(需要记住key名字符串")
print(f"namedtuple:{a_nt.amount} (IDE有自动补全)")

# 不可变性（namedtuple 不能改）
try:
    a_nt.amount = 999 # 不是AttributeError
except AttributeError as e:
    print(f"namedtuple 不可变:{e}")

# 内存对比
dict_size = sys.getsizeof(orders[0])
nt_size = sys.getsizeof(nt_orders[0])
print(f"\n 单个 dict内存:{dict_size}bytes")
print(f"50个总计：dict ≈ {dict_size * 50} bytes," f"namedtuple ≈ {nt_size * 50} bytes")

# 额外:defaultdict 嵌套用法
print("\n==== 各城市各品类销售额 ====")
city














