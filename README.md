# Fundamentals_of_layout_21_2

Учебный проект по верстке и работе с простым Python-сервером.

## 🚀 Запуск проекта

### 1. Клонировать репозиторий
```bash
git clone https://github.com/ArtemKabr/Fundamentals_of_layout_21_2.git
cd Fundamentals_of_layout_21_2

2. Создать виртуальное окружение
python -m venv .venv

3. Активировать окружение

Windows (PowerShell):

.venv\Scripts\activate


Linux/Mac:

source .venv/bin/activate

4. Запустить сервер
python server.py


После запуска сервер будет доступен по адресу:

http://localhost:8000

📂 Структура проекта
Fundamentals_of_layout_21_2/
├── frontend/
│   ├── index.html
│   ├── catalog.html
│   ├── contacts.html
│   ├── profile.html
│   ├── categorys/
│   │   ├── category-smartphones.html
│   │   ├── category-laptops.html
│   │   └── category-tech.html
│   └── img/
│       ├── smartphone.jpg
│       ├── laptop.jpg
│       └── tech.jpg
├── server.py
├── .gitignore
└── README.md