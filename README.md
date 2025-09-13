# Beyond the Event Horizon (За пределами горизонта событий)

![Game Icon](icon.ico)

**Визуальная новелла в жанре sci-fi horror**

[![Ren'Py](https://img.shields.io/badge/Engine-Ren'Py-orange)](https://www.renpy.org/)
[![Version](https://img.shields.io/badge/Version-1.0-green)](https://github.com)
[![Release Date](https://img.shields.io/badge/Release-01.09.2025-blue)](https://github.com)
[![Jam](https://img.shields.io/badge/Game%20Jam-100%20Flowers%20Jam%202025-purple)](https://vk.com/jamof100flowers)

## 📖 Описание

**Beyond the Event Horizon** - это визуальная новелла в жанре научной фантастики с элементами хоррора. История разворачивается на космической станции, где экипаж сталкивается с необъяснимыми событиями, которые ставят под угрозу их жизнь и рассудок.

Игра была разработана в рамках игрового джема "Джем ста цветов 2025" [vk.com/jamof100flowers](https://vk.com/jamof100flowers).

## 🛠 Установка и запуск

### Автоматическая установка
1. Скачайте архив игры с [Itch.io](https://featharine.itch.io/beyond-the-event-horizon)
2. Распакуйте архив в удобную папку
3. Запустите `Beyond_the_event_horizon.exe`

### Ручная установка из исходников
```bash
# Клонирование репозитория
git clone https://github.com/featharine/beyond-the-event-horizon.git

# Переход в директорию проекта
cd beyond-the-event-horizon

# Запуск через Ren'Py SDK
renpy.exe game/
```

## 🏗 Структура проекта

```
game/
├── audio/                 # Аудио файлы
│   ├── bg/               # Фоновая музыка
│   └── sfx/              # Звуковые эффекты
├── chapters/             # Основные главы сюжета
│   ├── day_0_prologue.rpy
│   ├── day_1.rpy
│   └── ...
├── configs/              # Конфигурационные файлы
│   ├── audio.rpy         # Настройки звука
│   ├── characters.rpy    # Определения персонажей
│   ├── definitions.rpy   # Константы и переменные
│   ├── gui.rpy          # Настройки интерфейса
│   ├── images.rpy       # Определения изображений
│   ├── options.rpy      # Основные настройки
│   └── transforms.rpy   # Анимационные трансформации
├── gui/                  # Графический интерфейс
│   ├── achievements/    # Иконки достижений
│   ├── bar/            # Полоски прогресса
│   ├── button/         # Кнопки интерфейса
│   ├── fonts/          # Шрифты
│   ├── menu/           # Элементы меню
│   └── phone/          # Телефонный интерфейс
├── images/              # Графические ресурсы
│   ├── Backgrounds/    # Фоновые изображения
│   ├── CG/            # Полноэкранные изображения
│   ├── Credits/       # Титры
│   └── [Персонажи]/   # Спрайты персонажей
├── minigames/          # Мини-игры
│   ├── assamble_puzzle/
│   ├── hanoi/
│   ├── lockpick/
│   ├── password_keyboard/
│   └── ...
├── scenes/             # Отдельные сцены
├── screens/            # Экраны интерфейса
├── scripts/            # Скрипты и модули
└── tl/                # Файлы перевода
```

## 🎵 Саундтрек

Музыка для игры была создана с использованием нейросети [Suno](https://suno.com)

## 👨‍💻 Команда разработчиков

- **Featharine** ([VK](https://vk.com/sweet_sour_figures)) - Сценарий, концепт, персонажи, CG, UI, музыка
- **Fataler** ([Steam](https://steamcommunity.com/id/fataler)) - Код, мини-игры, редактура, анимации
- **Kapushishin** ([Steam](https://steamcommunity.com/id/Kapushishin)) - Фоны, сборка новеллы, сбор референсов, режиссура, звуки

## 📚 Использованные ресурсы

### Шрифты
- [Lora](https://fonts.google.com/specimen/Lora/) - основной шрифт
- [Pixeloid Sans](https://fonts-online.ru/fonts/pixeloid-sans) - моноширинный шрифт

### Звуковые эффекты
- [Freesound.org](https://freesound.org/) - 130+ звуковых эффектов
- [Atelier Magicae](https://ateliermagicae.itch.io/be-not-afraid-uimenu-sfx) - UI звуки
- [Hove Audio](https://hoveaudio.itch.io/free-sci-fi-ui-sound-effects-pack) - Sci-fi звуки

Полный список используемых ресурсов находится в файле `external_resources.txt`.

## 📝 Лицензия

Игра распространяется бесплатно. Использованные сторонние ресурсы имеют соответствующие лицензии (CC BY, CC0 и др.).

## 🌟 Благодарности

- Сообществу Ren'Py за отличный движок
- Участникам джема "100 цветов" за вдохновение
- Всем, кто помогал с тестированием и обратной связью