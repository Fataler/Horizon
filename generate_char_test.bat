@echo off
chcp 65001 > nul
setlocal

REM =================================================================
REM Батник для генерации тестов состояний персонажей Ren'Py
REM =================================================================
REM
REM Поместите этот файл в корневую директорию вашего проекта.
REM
REM Использование:
REM   generate_char_test.bat [имя_layeredimage]
REM
REM Пример:
REM   generate_char_test.bat r_f
REM
REM =================================================================

REM --- Конфигурация ---
set SCRIPT_PATH=game\tests\character_test_generator.py
set CHAR_CONFIG_PATH=game\configs\characters.rpy
set OUTPUT_DIR=game\tests
set DEFAULT_BG=black
REM --------------------

set "CHARACTER_NAME=%~1"

if not defined CHARACTER_NAME (
    echo.
    echo Ошибка: Имя layeredimage персонажа не указано.
    echo.
    echo   Использование: %~n0 [имя_layeredimage]
    echo   Пример:      %~n0 r_f
    echo.
    goto :eof
)

set "OUTPUT_FILE=%OUTPUT_DIR%\test_%CHARACTER_NAME%_states.rpy"

echo.
echo =================================================
echo  Генерация теста для персонажа: %CHARACTER_NAME%
echo =================================================
echo.
echo  - Скрипт: %SCRIPT_PATH%
echo  - Файл персонажей: %CHAR_CONFIG_PATH%
echo  - Выходной файл: %OUTPUT_FILE%
echo.

if not exist "%SCRIPT_PATH%" (
    echo Ошибка: Скрипт-генератор не найден по пути: %SCRIPT_PATH%
    goto :eof
)

if not exist "%CHAR_CONFIG_PATH%" (
    echo Ошибка: Файл с определениями персонажей не найден: %CHAR_CONFIG_PATH%
    goto :eof
)


python "%SCRIPT_PATH%" -i "%CHAR_CONFIG_PATH%" -n "%CHARACTER_NAME%" -o "%OUTPUT_FILE%" -c "%CHARACTER_NAME%" -bg "%DEFAULT_BG%"

if %errorlevel% neq 0 (
    echo.
    echo !!! Произошла ошибка во время выполнения скрипта.
    echo.
) else (
    echo.
    echo --- Успешно! ---
    echo Тест сохранен в: %OUTPUT_FILE%
    echo.
)

pause
