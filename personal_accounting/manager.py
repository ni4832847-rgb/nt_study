from datetime import datetime

from record import Record
from storage import add_record, delete_record, get_summary, load_records, update_record,search_records_by_date


def _print_record(record):
    print(
        f"编号：{record.record_id}\n"
        f"类型：{record.record_type}\n"
        f"金额：{record.amount}\n"
        f"分类：{record.category}\n"
        f"备注：{record.description}\n"
        f"日期：{record.record_date}\n"
        f"创建时间：{record.created_at}\n"
    )


def create_record():
    record_type = input("请输入类型（income/expense）：").strip()

    if record_type not in ("income", "expense"):
        print("类型只能是 income 或 expense")
        return

    try:
        amount = float(input("请输入金额：").strip())
    except ValueError:
        print("金额必须是数字")
        return

    if amount <= 0:
        print("金额必须大于 0")
        return

    summary = get_summary()
    balance = summary["balance"]

    if record_type == "expense" and amount > balance:
        print(f"余额不足，当前余额：{balance}")
        return

    category = input("请输入分类：").strip()
    if not category:
        print("分类不能为空")
        return

    description = input("请输入备注：").strip()
    record_date = input("请输入日期（YYYY-MM-DD）：").strip()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    record = Record(
        record_id=None,
        record_type=record_type,
        amount=amount,
        category=category,
        description=description,
        record_date=record_date,
        created_at=created_at,
    )

    new_id = add_record(record)
    print(f"新增成功，编号：{new_id}")

    if record_type == "expense":
        print(f"当前余额: {balance - amount}")
    else:
        print(f"当前余额: {balance + amount}")


def list_records():
    records = load_records()

    if not records:
        print("当前没有账单记录")
        return

    for record in records:
        _print_record(record)


def remove_record():
    try:
        record_id = int(input("请输入要删除的账单编号：").strip())

    except ValueError:
        print("编号必须是数字")
        return

    deleted_count = delete_record(record_id)

    if deleted_count > 0:
        print("删除成功")
    else:
        print("没有找到这条账单")


def edit_record():
    records = load_records()

    try:
        record_id = int(input("请输入要修改的账单编号：").strip())
    except ValueError:
        print("编号必须是数字")
        return

    target_record = None

    for record in records:
        if record.record_id == record_id:
            target_record = record
            break

    if target_record is None:
        print("没有找到这条账单")
        return

    print("找到原账单：")
    _print_record(target_record)

    record_type = input("请输入新的类型（income/expense）：").strip()
    if record_type not in ("income", "expense"):
        print("类型只能是 income 或 expense")
        return

    try:
        amount = float(input("请输入新的金额：").strip())
    except ValueError:
        print("金额必须是数字")
        return

    if amount <= 0:
        print("金额必须大于 0")
        return

    summary = get_summary()
    available_balance = summary["balance"]

    if target_record.record_type == "income":
        available_balance -= target_record.amount
    elif target_record.record_type == "expense":
        available_balance += target_record.amount

    if record_type == "expense" and amount > available_balance:
        print(f"余额不足，当前可用余额：{available_balance}")
        return

    category = input("请输入新的分类：").strip()
    if not category:
        print("分类不能为空")
        return

    description = input("请输入新的备注：").strip()
    record_date = input("请输入新的日期（YYYY-MM-DD）：").strip()

    target_record.record_type = record_type
    target_record.amount = amount
    target_record.category = category
    target_record.description = description
    target_record.record_date = record_date

    update_count = update_record(target_record)

    if update_count > 0:
        print("修改成功")

        if record_type == "expense":
            print(f"当前余额: {available_balance - amount}")
        else:
            print(f"当前余额: {available_balance + amount}")

    else:
        print("修改失败")


def show_summary():
    summary = get_summary()
    print(f"总收入: {summary['income']}")
    print(f"总支出: {summary['expense']}")
    print(f"当前余额: {summary['balance']}")




def search_by_date():
    record_date = input("请输入要查询的日期(YYYY-MM-DD):").strip()

    records = search_records_by_date(record_date)
    if not records:
        print("没有找到这个日期的账单")
        return

    for record in records:
        _print_record(record)






