# import asyncio
# import json
# import random
# from dataclasses import dataclass
# from datetime import datetime
# from pathlib import Path
#
# import yaml
#
#
# BASE_DIR = Path(__file__).resolve().parent
# DATA_DIR = BASE_DIR / "data"
# CONFIG_PATH = DATA_DIR / "config.yaml"
# PRODUCTS_PATH = DATA_DIR / "products.json"
# REPORT_PATH = DATA_DIR / "report.json"
#
#
# @dataclass
# class Product:
#     """生鲜商品。"""
#
#     id: str
#     name: str
#     price: float
#     stock: int
#
#     def sell(self, qty: int) -> None:
#         if qty > self.stock:
#             raise ValueError(f"库存不足：{self.name} 剩余 {self.stock}，需要 {qty}")
#         self.stock -= qty
#
#     def restock(self, qty: int) -> None:
#         self.stock += qty
#
#     def info(self) -> str:
#         return f"[{self.id}] {self.name} - ￥{self.price:.2f}（库存：{self.stock}）"
#
#     def __str__(self) -> str:
#         return self.info()
#
#
# def load_yaml(path: Path) -> dict:
#     with path.open("r", encoding="utf-8") as file:
#         return yaml.safe_load(file)
#
#
# def load_products(path: Path) -> list[Product]:
#     with path.open("r", encoding="utf-8") as file:
#         data = json.load(file)
#
#     return [
#         Product(
#             product_id["id"],
#             product_id["name"],
#             float(product_id["price"]),
#             int(product_id["stock"]),
#         )
#         for product_id in data["products"]
#     ]
#
#
# def calculate_actual_cost(price: float) -> float:
#     """计算加上 5% 损耗后的实际成本。"""
#     return round(price * 1.05, 2)
#
#
# async def query_warehouse_stock(
#     warehouse: str,
#     base_url: str,
#     products: list[Product],
# ) -> dict:
#     """模拟查询一个前置仓的库存。"""
#     delay = random.uniform(1, 2)
#     await asyncio.sleep(delay)
#
#     return {
#         "warehouse": warehouse,
#         "request_url": f"{base_url}/warehouses/{warehouse}/inventory",
#         "elapsed_seconds": round(delay, 2),
#         "stocks": {product.id: product.stock for product in products},
#     }
#
#
# async def query_all_warehouses(
#     base_url: str,
#     timeout: float,
#     products: list[Product],
# ) -> list[dict]:
#     warehouses = ["浦东仓", "徐汇仓", "闵行仓"]
#     tasks = [
#         query_warehouse_stock(warehouse, base_url, products)
#         for warehouse in warehouses
#     ]
#     return await asyncio.wait_for(asyncio.gather(*tasks), timeout=timeout)
#
#
# def build_product_report(products: list[Product]) -> list[dict]:
#     return [
#         {
#             "id": product.id,
#             "name": product.name,
#             "price": product.price,
#             "actual_cost": calculate_actual_cost(product.price),
#             "stock": product.stock,
#         }
#         for product in products
#     ]
#
#
#
#
# async def main() -> None:
#     config = load_yaml(CONFIG_PATH)
#     api_config = config["api"]
#     base_url = api_config["base_url"]
#     timeout = float(api_config["timeout"])
#
#     products = load_products(PRODUCTS_PATH)
#     warehouse_inventory = await query_all_warehouses(
#         base_url,
#         timeout,
#         products,
#     )
#
#     report = {
#         "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
#         "api": {
#             "base_url": base_url,
#             "timeout": timeout,
#         },
#         "products": build_product_report(products),
#         "warehouse_inventory": warehouse_inventory,
#     }
#
#     with REPORT_PATH.open("w", encoding="utf-8") as file:
#         json.dump(report, file, ensure_ascii=False, indent=2)
#
#     print(f"已生成库存报告：{REPORT_PATH}")
#     print(f"商品数量：{len(products)}，前置仓数量：{len(warehouse_inventory)}")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

