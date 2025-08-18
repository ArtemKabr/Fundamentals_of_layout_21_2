import os
from http.server import HTTPServer, BaseHTTPRequestHandler

BASE_DIR = os.path.join(os.path.dirname(__file__), "frontend")

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Обрабатываем GET-запросы и отдаем статические страницы"""
        routes = {
            "/": "index.html",
            "/index.html": "index.html",
            "/catalog.html": "catalog.html",
            "/category.html": "category.html",
            "/contacts.html": "contacts.html",
            "/profile.html": "profile.html",
        }

        path = self.path

        # Если путь есть в словаре маршрутов
        if path in routes:
            filename = routes[path]
            file_path = os.path.join(BASE_DIR, filename)
        else:
            # иначе пробуем открыть как файл из папки frontend
            file_path = os.path.join(BASE_DIR, path.lstrip("/"))

        # Проверяем существование файла
        if os.path.isfile(file_path):
            self.send_response(200)

            # определяем content-type
            if file_path.endswith(".html"):
                content_type = "text/html; charset=utf-8"
            elif file_path.endswith(".css"):
                content_type = "text/css"
            elif file_path.endswith(".js"):
                content_type = "application/javascript"
            elif file_path.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                content_type = "image/" + file_path.split(".")[-1]
                if file_path.endswith(".jpg"):
                    content_type = "image/jpeg"
            else:
                content_type = "application/octet-stream"

            self.send_header("Content-type", content_type)
            self.end_headers()

            # читаем правильно (текст = utf-8, картинки = бинарно)
            if "image" in content_type or content_type.startswith("application/"):
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                with open(file_path, "r", encoding="utf-8") as f:
                    self.wfile.write(f.read().encode("utf-8"))

        else:
            self.send_error(404, "File Not Found")

    def do_POST(self):
        """Обрабатываем POST-запрос — печатаем данные формы в консоль"""
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode("utf-8")
        print("📩 Получены данные:", post_data)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>Спасибо за сообщение!</h1>".encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), SimpleHandler)
    print("🚀 Сервер запущен: http://localhost:8000")
    server.serve_forever()
