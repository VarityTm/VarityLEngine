@echo off
setlocal enabledelayedexpansion

:: Проверка прав администратора
openfiles >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [!] ОШИБКА: Запустите этот файл ОТ ИМЕНИ АДМИНИСТРАТОРА.
    echo.
    pause
    exit /b
)

:: Укажите имя вашего EXE файла здесь
set "EXE_NAME=VarityEngine.exe"
set "EXE_PATH=%~dp0%EXE_NAME%"

:: Проверка наличия EXE
if not exist "%EXE_PATH%" (
    echo.
    echo [!] ОШИБКА: Файл %EXE_NAME% не найден в этой папке.
    echo Сначала скомпилируйте Python-скрипт в EXE.
    echo.
    pause
    exit /b
)

echo [+] Настройка расширения .var...

:: Регистрация типа файла
assoc .var=VarityFile
ftype VarityFile="%EXE_PATH%" "%%1"

:: Добавление иконки (берется первая иконка из EXE)
reg add "HKEY_CLASSES_ROOT\VarityFile\DefaultIcon" /t REG_SZ /d "%EXE_PATH%,0" /f >nul

echo.
echo =========================================
echo Готово! Теперь файлы .var открываются 
echo двойным кликом через %EXE_NAME%.
echo =========================================
echo.
pause