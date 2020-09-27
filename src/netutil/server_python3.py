#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.server as s
import json
from urllib.parse import parse_qs
from urllib.parse import urlparse


class MyHandler(s.BaseHTTPRequestHandler):
    def do_POST(self):
        self.make_data("post")

    def do_GET(self):
        self.make_data("get")

    def make_data(self, method: str):
        # request
        if method == 'post':
            try:
                # urlパラメータを取得
                parsed = urlparse(self.path)
                # urlパラメータを解析
                params: dict = parse_qs(parsed.query)
                # body部を取得
                content_len = int(self.headers.get("content-length"))
                req_body: str = self.rfile.read(content_len).decode("utf-8")
                pass
            except Exception as e:
                print(e)
                try:
                    self.send_response(500)
                except Exception as e2:
                    print(e2)
        # response
        if method in ["post", "get"]:
            try:
                # response data
                res_json_dict: dict = self.make_response_data(method)
                res_json_binary: bytes = json.dumps(res_json_dict, sort_keys=True, ensure_ascii=False, indent=2).encode(
                    "utf-8")
                self.send_response(200)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(res_json_binary)
                pass
            except Exception as e:
                print(e)
                self.send_response(500)
            pass
        else:
            print("not support method. {}".format(method))
            try:
                self.send_response(500)
            except Exception as e2:
                print(e2)

    @staticmethod
    def make_response_data(http_method: str) -> dict:
        res: dict = {
            "code": 200,
            "http_method": http_method,
            "msg": "success"
        }
        return res


host = '0.0.0.0'
port = 8000
httpd = s.HTTPServer((host, port), MyHandler)
print('サーバを起動しました。ポート:%s' % port)
httpd.serve_forever()
