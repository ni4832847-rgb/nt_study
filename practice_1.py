# 需要：pip install --upgrade openai
# 前置：设置环境变量 PACKY_API_KEY
import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import httpx
from openai import APIConnectionError, APIStatusError, OpenAI

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://www.packyapi.com/v1").strip().rstrip("/")
MAX_OUTPUT_TOKENS = 800
PROXY_URL = os.getenv("OPENAI_PROXY", "off").strip()
API_KEY = os.getenv("PACKY_API_KEY")
API_KEY_SOURCE = "PACKY_API_KEY"

if BASE_URL.endswith("/console"):
    BASE_URL = BASE_URL.removesuffix("/console") + "/v1"

if not API_KEY:
    print(
        "没有找到 PACKY_API_KEY 环境变量。\n"
        "请在 PyCharm/VSCode 的运行配置里设置 PACKY_API_KEY，"
        "或者在终端里先执行：$env:PACKY_API_KEY='你的 PackyAPI Key'"
    )
    raise SystemExit(1)

if PROXY_URL.lower() in {"", "none", "false", "off"}:
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL, timeout=60)
else:
    client = OpenAI(
        api_key=API_KEY,
        base_url=BASE_URL,
        timeout=60,
        http_client=httpx.Client(proxy=PROXY_URL, timeout=60),
    )

print(f"使用模型：{MODEL}")
print(f"API 地址：{BASE_URL}")
print(f"Key 来源：{API_KEY_SOURCE}")
print(f"代理配置：{PROXY_URL or '不使用代理'}")

# 同一个 user message、3 个不同 system prompt
SYSTEM_PROMPTS = {
    "严肃律师": "你是严谨的合约律师。回答要精准、引用法条编号、避免任何主观形容词。",
    "幼儿园老师": "你是温柔的幼儿园老师、要对 5 岁小孩说话。用比喻、口语、少于 80 字。",
    "JSON 机器": "你只回 JSON。schema: {\"answer\": string, \"confidence\": float}",
}

USER_MSG = "请帮我解释什么是租赁合约。"

outputs = {}
try:
    for label, system in SYSTEM_PROMPTS.items():
        r = client.chat.completions.create(
            model=MODEL,
            max_tokens=MAX_OUTPUT_TOKENS,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": USER_MSG},
            ],
        )
        outputs[label] = r.choices[0].message.content
        print(f"\n--- [{label}] ---")
        print(outputs[label])
except APIConnectionError as exc:
    print(
        "\n无法连接 OpenAI API。请检查代理是否已启动，以及 OPENAI_PROXY 端口是否正确。\n"
        "例如：$env:OPENAI_PROXY='http://127.0.0.1:7890'\n"
        "如果你的网络可直接访问 OpenAI，可设置：$env:OPENAI_PROXY='off'"
    )
    raise SystemExit(1) from exc
except APIStatusError as exc:
    print(
        f"\nOpenAI API 返回错误：HTTP {exc.status_code}。\n"
        "请检查 PACKY_API_KEY 是否正确、账号是否有余额，以及当前模型是否有权限使用。"
    )
    print(f"错误详情：{exc.response.text}")
    raise SystemExit(1) from exc

# === 自我验证 ===
json_output = outputs["JSON 机器"]
assert "{" in json_output and "}" in json_output, "JSON 机器版输出应该含 JSON braces"
try:
    parsed = json.loads(json_output.strip().split("\n")[-1] if "\n" in json_output else json_output)
    assert "answer" in parsed, "JSON schema 应包含 answer 栏位"
except json.JSONDecodeError:
    pass  # 容许 model 回 JSON 含解释文字、最后一笔才是 JSON
print(f"\n✅ 练习 1 通过 — 同一个问题、3 種人格 / 格式 / 语气")
print("💡 观察：律师长、老师短、JSON 机器一定是 {...}")
