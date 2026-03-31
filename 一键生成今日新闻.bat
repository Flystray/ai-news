@echo off
chcp 65001 > nul
echo ========================================
echo    🤖 AI新闻采集与报告生成工具
echo ========================================
echo.

cd /d "%~dp0"

echo 📅 当前日期: %date%
echo.

echo 🔍 开始采集新闻并生成带链接的报告...
echo.

REM 使用Python运行采集脚本（如果安装了Python）
where python >nul 2>&1
if %errorlevel%==0 (
    echo ✓ Python 已安装，开始执行...
    python collect_news.py
) else (
    echo ⚠ Python 未安装，请手动访问以下链接查看新闻:
    echo.
    echo 📰 科技媒体:
    echo    • 量子位: https://www.qbitai.com/
    echo    • 机器之心: https://jiqizhixin.com/
    echo.
    echo 📱 AI大厂:
    echo    • 通义博客: https://qwenlm.github.io/blog/
    echo    • OpenAI: https://openai.com/blog
    echo    • DeepMind: https://deepmind.google/discover/blog/
    echo.
)

echo.
echo ========================================
echo    ✅ 完成！
echo ========================================
echo.
echo 📁 报告目录: %~dp0reports\
echo.

REM 打开报告目录
explorer "%~dp0reports\"

pause
