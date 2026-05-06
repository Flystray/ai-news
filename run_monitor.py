# -*- coding: utf-8 -*-
"""Wrapper to run creator_monitor.py and capture all output."""
import sys
import io
import traceback
import datetime

sys.path.insert(0, r"C:\Users\YF\.workbuddy\skills\ai-news")

buf = io.StringIO()
try:
    from creator_monitor import main
    with __import__('contextlib').redirect_stdout(buf), __import__('contextlib').redirect_stderr(buf):
        try:
            date_str = sys.argv[1] if len(sys.argv) > 1 else datetime.datetime.now().strftime("%Y-%m-%d")
            result = main(date_str)
            print(f"\n__RESULT__:{result}")
        except SystemExit as e:
            print(f"\n__EXIT__:{e.code}")
        except Exception as e:
            print(f"\n__ERROR__:{e}")
            traceback.print_exc()
    output = buf.getvalue()
    # Write to file for inspection
    with open(r"C:\Users\YF\.workbuddy\skills\ai-news\monitor_output.txt", "w", encoding="utf-8") as f:
        f.write(output)
    print("Output written to monitor_output.txt")
    print(f"Length: {len(output)} chars")
    # Also print last part of output
    print("=== LAST 2000 CHARS ===")
    print(output[-2000:] if len(output) > 2000 else output)
except Exception as e:
    print(f"Wrapper error: {e}")
    traceback.print_exc()
