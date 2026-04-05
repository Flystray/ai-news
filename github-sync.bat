@echo off
chcp 65001 > nul
echo ========================================
echo    🔄 GitHub 同步工具
echo ========================================
echo.

cd /d "%~dp0"

REM ============ 提交并推送 ============
git add .
git commit -m "Update AI News: %date%"
git push origin main

echo.
echo ? 同步完成！
echo ? 在线查看: https://Flystray.github.io/ai-news/

echo.
pause
