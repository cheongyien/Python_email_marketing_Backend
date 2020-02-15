import os
import tornado.ioloop
import tornado.web as web
import webbrowser
import start_smtp_server

public_root = os.path.join(os.path.dirname(__file__), './public/')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class authenticateHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('email_content.html')


handlers = [
    (r'/', MainHandler),
    (r'/authenticate', authenticateHandler),
    (r'/', web.StaticFileHandler, {'path': public_root}),
]

settings = dict(
    static_path=public_root,
    template_path=public_root
)

application = web.Application(handlers, **settings)

if __name__ == "__main__":
    http_port = 7777
    print(f"Starting HTTP Server at port {http_port}")
    application.listen(http_port)
    server = start_smtp_server.start_server()
    webbrowser.open_new_tab(f"http://localhost:{http_port}/")
    tornado.ioloop.IOLoop.instance().start()
