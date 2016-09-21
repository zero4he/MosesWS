#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib

from flask import Flask, request, Response, jsonify, abort

app = Flask(__name__)

'''
start moses server:

~/mosesdecoder/bin/moses  --server -f ~/working/binarised-model/moses.ini --server-port 8080 --server-log server.log --daemon

install Flask:

pip install Flask

'''


@app.route('/')
def home():
    return "Welcome to MarsTranslate"


@app.route('/translate')
def translate():
    url = "http://192.168.1.147:8080/RPC2"
    proxy = xmlrpclib.ServerProxy(url)

    # text = u"je suis un homme."
    if 'text' not in request.args:
        return jsonify({'code': 400, 'errmsg': "'text' is require"}), 400

    params = {"text": request.args["text"], "word-align": "true", "align": "false"}
    result = proxy.translate(params)

    return jsonify(result)


if __name__ == '__main__':
    app.run()
