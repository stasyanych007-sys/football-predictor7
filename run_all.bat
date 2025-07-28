@echo off
echo Запуск сервера Flask...
start "Flask Server" cmd /k "python app.py"

echo Ожидание запуска сервера...
timeout /t 5 >nul

echo Тест API...
python test_api.py

pause
