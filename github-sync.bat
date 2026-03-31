@echo off
chcp 65001 > nul
echo ========================================
echo    🔄 GitHub 同步工具
echo ========================================
echo.

cd /d "%~dp0"

REM 检查git状态
git status > nul 2>&1
if %errorlevel% neq 0 (
    echo 📦 初始化Git仓库...
    git init
    git add .
    git commit -m "Update AI News: %date%"
    echo.
    echo ⚠️ 请先关联远程仓库:
    echo    git remote add origin https://github.com/Flystray/ai-news.git
    echo    git push -u origin main
) else (
    echo 🔍 检查更改...
    git status --short
    
    echo.
    echo 📤 提交更改...
    git add .
    git commit -m "Update AI News: %date%"
    
    echo.
    echo 🚀 推送到GitHub...
    git push
    
    echo.
    echo ✅ 同步完成！
    echo 🌐 访问: https://Flystray.github.io/ai-news/
)

echo.
pause
