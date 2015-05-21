#Lots of code blatantly stolen from the Websocket demo included with
#Tornado

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid

class DoThat(tornado.web.RequestHandler):
    def get(self):
        self.write("THIS IS ANOTHER PAGE")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=ComSocket.cache)

class someMessage(tornado.web.RequestHandler):
    def post(self):
        message = {
            "id": "SOMEID",
            "from": "I GUESS A USER",
            "body": "LIKE I CARE"
        }
        message["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=message))
        if self.get_argument("next", None):
            self.redirect(self.get_argument("next"))
        else:
            self.write(message)

myapplication = tornado.web.Application([
    (r"/", MainHandler),
    (r"/somepage", DoThat),
    (r"/MESSAGING", someMessage)
    ]
    )



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/somepage", DoThat),
            (r"/MESSAGING", someMessage),
            (r"/ComSocket", ComSocket)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class ComSocket(tornado.websocket.WebSocketHandler):
    waiters = set()
    cache = []
    cache_size = 100

    def open(self):
        #ANYTIME SOMEONE JOINS
        ComSocket.waiters.add(self)

    def on_close(self):
        #ANYTIME SOMEONE LEAVES (How do we know?)
        ComSocket.waiters.remove(self)

    def on_message(self, message):
        #ANYTIME WE GET A HIT FROM SOMETHING
        parsed = tornado.escape.json_decode(message)
        chat = {
            "id": str(uuid.uuid4()),
            "body": parsed["body"]
            }
        chat["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=chat))
        print("Some message just happened")

        ComSocket.update_cache(chat)
        ComSocket.send_updates(chat)

    @classmethod
    def send_updates(cls, chat):
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except:
                print("COULD NOT SEND MESSAGE")

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]
        
        

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
