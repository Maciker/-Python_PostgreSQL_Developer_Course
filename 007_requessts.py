Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> requests.get('http://www.example.com')
<Response [200]>
>>> r = requests.get('http://www.example.com')
>>> r
<Response [200]>
>>> r.content
b'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 50px;\n        background-color: #fff;\n        border-radius: 1em;\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        body {\n            background-color: #fff;\n        }\n        div {\n            width: auto;\n            margin: 0 auto;\n            border-radius: 0;\n            padding: 1em;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is established to be used for illustrative examples in documents. You may use this\n    domain in examples without prior coordination or asking for permission.</p>\n    <p><a href="http://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'
>>> r = requests.get('https://api.twitter.com/1.1/custom_profiles/:id.json')
>>> r
<Response [404]>
>>> r = requests.get('https://api.twitter.com/1.1/custom_profiles/:id.json')
>>> r
<Response [404]>
>>> r.content
b'{"errors":[{"message":"Sorry, that page does not exist","code":34}]}'
>>> r = requests.get('https://api.twitter.com/1.1/direct_messages/events/show.json')
>>> r
<Response [400]>
>>> r.content
b'{"errors":[{"code":215,"message":"Bad Authentication data."}]}'
>>> 
