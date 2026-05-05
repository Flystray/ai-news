#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import json
from pathlib import Path

SKILL_DIR = Path(r"C:\Users\YF\.workbuddy\skills\ai-news")
CREATORS_FILE = SKILL_DIR / "creators.json"

print("调试：开始测试...", flush=True)

# 测试读取 creators.json
try:
    with open(CREATORS_FILE, "r", encoding="utf-8") as f:
        creators_data = json.load(f)
    print(f"调试：读取 creators.json 成功，keys: {list(creators_data.keys())}", flush=True)
except Exception as e:
    print(f"调试：读取失败: {e}", flush=True)
    sys.exit(1)

# 测试访问 platforms
try:
    platforms = creators_data.get("platforms", {})
    print(f"调试：platforms keys: {list(platforms.keys())}", flush=True)
except Exception as e:
    print(f"调试：访问 platforms 失败: {e}", flush=True)
    sys.exit(1)

# 测试访问 platforms["youtube"]
try:
    yt_section = platforms["youtube"]
    print(f"调试：youtube section keys: {list(yt_section.keys())}", flush=True)
    print(f"调试：youtube creators 数量: {len(yt_section.get('creators', []))}", flush=True)
except Exception as e:
    print(f"调试：访问 youtube 失败: {e}", flush=True)
    sys.exit(1)

print("调试：所有测试通过！", flush=True)
