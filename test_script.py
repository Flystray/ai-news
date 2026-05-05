#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
print("调试：脚本开始执行", flush=True)
print(f"Python 版本: {sys.version}", flush=True)

# 测试导入
try:
    import json
    print("json 导入成功", flush=True)
except Exception as e:
    print(f"json 导入失败: {e}", flush=True)

try:
    from pathlib import Path
    print("pathlib 导入成功", flush=True)
except Exception as e:
    print(f"pathlib 导入失败: {e}", flush=True)

# 测试文件读取
try:
    from pathlib import Path
    SKILL_DIR = Path(r"C:\Users\YF\.workbuddy\skills\ai-news")
    CREATORS_FILE = SKILL_DIR / "creators.json"
    with open(CREATORS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"成功读取 creators.json，有 {len(data.get('platforms', {}))} 个平台", flush=True)
except Exception as e:
    print(f"读取文件失败: {e}", flush=True)

print("调试：脚本执行完毕", flush=True)
