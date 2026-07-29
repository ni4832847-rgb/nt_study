# Python Todo Practice

这是一个用于练习 Python、Git、pytest 的命令行任务管理项目。

## 功能

- 查看任务
- 新增任务
- 删除任务
- 标记任务完成
- 保存任务到 JSON 文件
- 从 JSON 文件读取任务
- 使用 pytest 测试工具函数

## 项目结构

```text
todo/
  todo.py              # 主程序入口
  task_utils.py        # 任务管理工具函数
  test_task_utils.py   # pytest 测试文件
  tasks.json           # 任务数据文件
  requirements.txt     # 项目依赖