# -*- coding: utf-8 -*-
from typing import Optional, Awaitable

import tornado.ioloop
import tornado.web
import importlib
import common.utils
import logging
import traceback
from tornado import httpserver, options, gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from configuration.config import Config


class MainHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=20)

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    @run_on_executor
    def run_api(self, module, action, args):
        try:
            module = importlib.import_module('modules.%s.controller' % module)
            r = module.dispatcher(self, action, **args)
            return r
        except Exception as e:
            logging.error(traceback.format_exc())
            return dict(status="fail", message="系统错误", data="SERVER error: {0}".format(e))

    @gen.coroutine
    def get(self, module, action):
        args = common.utils.format_args_get(self.request.query_arguments)
        res = yield self.run_api(module, action, args)
        # self.set_header("Access-Control-Allow-Origin", "*")
        # self.set_header("Access-Control-Allow-Headers", "application/json, text/plain, */*")
        # self.set_header("Access-Control-Allow-Methods", "POST, GET, PUT, DELETE, OPTIONS")
        # self.set_header("Access-Control-Allow-Credentials", "true")
        self.write(res)


if __name__ == "__main__":
    options.define('env', default="dev", help='app running environment', type=str)
    options.define("port", default=8888, help="run on the given port", type=int)
    options.parse_command_line()

    env = options.options.env
    Config.set_config_env(env)

    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    app_handler = logging.handlers.TimedRotatingFileHandler(Config.get_config().LOG_PATH, 'D', 1, 10)
    app_log = logging.getLogger()
    app_handler.setFormatter(log_formatter)
    app_log.addHandler(app_handler)

    settings = dict(
        cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        debug=True,
        autoreload=True
    )
    handlers = [
        (r'/api/(.*)/(.*)', MainHandler),
    ]
    application = tornado.web.Application(handlers, **settings)
    port = options.options.port
    server = httpserver.HTTPServer(application, max_buffer_size=1048576000)
    server.bind(port)
    server.start()

    print('Web server started on port %d' % port)
    print('Press "Ctrl+C" to exit.\n')

    tornado.ioloop.IOLoop.current().start()
