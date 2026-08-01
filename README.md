# Python Todo Practice

这是一个用于练习 Python、Git、pytest 的命令行任务管理项目。

## 功能

- 查看任务
- 新增任务
- 删除任务
- 标记任务完成
- 搜索任务
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
```

## 安装依赖

进入 todo 目录：

```powershell
cd todo
```

创建虚拟环境：

```powershell
python -m venv .venv
```

激活虚拟环境：

```powershell
.\.venv\Scripts\Activate.ps1
```

安装依赖：

```powershell
pip install -r requirements.txt
```

## 运行程序

```powershell
python todo.py
```

## 运行测试

```powershell
.\.venv\Scripts\python.exe -m pytest
```

## 学习内容

这个项目练习了：

- Python 变量、列表、字典、函数、模块
- JSON 文件读写
- 异常处理
- pytest 基础测试
- Git 初始化、提交、分支、合并、冲突解决
- GitHub 远程仓库推送


## 备注
这是通过github网页添加的内容。

这是本地克隆仓库中添加的内容。

本项目会持续补充更多 python 和 git 练习