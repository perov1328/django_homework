
# Импорт необходимых библиотек для работы программы
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Определение настроек запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080   # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """
    def __get_html_content(self):
        with open("index.html", "r", encoding="utf-8") as file:
            content = file.read().replace("\n", "")
            return content

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)    # Код ответа
        self.send_header("Content-type", "text/html")   # Тип данных, которые мы передаем
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))    # Кодировка контента

if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
