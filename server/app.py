# Simple JSON Fetching server writtern on Flask - Python
# Author : DanBrown47
# Project : Docker

import flask
from flask import request,jsonify
import urllib.request
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return """
        <h1 id="docker-stuff">Docker stuff</h1>
        <p>Backend to process api from dockerhub</p>
        <h2 id="usage">Usage</h2>
        <pre><code class="lang-bash">curl -X GET http:<span class="hljs-regexp">//</span>&lt;IP&gt;<span class="hljs-regexp">/docker/</span>api<span class="hljs-regexp">/search/</span>repo<span class="hljs-regexp">/?query=</span>
        </code></pre>
        <blockquote>
        <p>Will return stuff in JSON</p>
        </blockquote>
        <p>The end ...</p>
    """

@app.route('/docker/api/search/repo/', methods=['GET'])
def api():
    query_in = request.args.get("query")
    url = "https://hub.docker.com/v2/search/repositories/?query="+query_in
    data = urllib.request.urlopen(url).read().decode()
    obj = json.loads(data)
    return obj
app.run()