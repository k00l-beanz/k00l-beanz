# Weather App

## Information Gathering

This appears to be a basic web application utilizing the Express JavaScript framework. 

Landing on `index.html` displays the current weather for my area. This means there is probably some third-party service the application is making a request to in order to retrieve this information.

Let's take a look at the project structure:

```s
$ tree
.
├── build-docker.sh
├── challenge
│   ├── database.js
│   ├── flag
│   ├── helpers
│   │   ├── HttpHelper.js
│   │   └── WeatherHelper.js
│   ├── index.js
│   ├── package.json
│   ├── package-lock.json
│   ├── routes
│   │   └── index.js
│   ├── static
│   │   ├── css
│   │   │   └── main.css
│   │   ├── favicon.gif
│   │   ├── host-unreachable.jpg
│   │   ├── js
│   │   │   ├── koulis.js
│   │   │   └── main.js
│   │   ├── koulis.gif
│   │   └── weather.gif
│   ├── views
│   │   ├── index.html
│   │   ├── login.html
│   │   └── register.html
│   └── weather-app.db
├── config
│   └── supervisord.conf
├── Dockerfile
├── package.json
├── package-lock.json
└── solve
    └── README.md

10 directories, 25 files
```

There are a few interesting files such as `helpers/HttpHelper.js`, `helpers/WeatherHelper.js`, `database.js`, `routes/index.js`. Looks like the flag is also sitting somewhere on the web server. This means we'll probably need to perform a server-side attack. Let's dig into the code.

Lastly, it's important to keep in mind the backend DBMS is sqlite3.

## Marination

### database.js

Immediately, I spot a SQLi with a nice little hint:

```js
async register(user, pass) {
    // TODO: add parameterization and roll public
    return new Promise(async (resolve, reject) => {
        try {
            let query = `INSERT INTO users (username, password) VALUES ('${user}', '${pass}')`;
            resolve((await this.db.run(query)));
        } catch(e) {
            reject(e);
        }
    });
}
```

Lets note this down and continue reading through the code.

Within the same file, I see the following function:

```js
async isAdmin(user, pass) {
    return new Promise(async (resolve, reject) => {
        try {
            let smt = await this.db.prepare('SELECT username FROM users WHERE username = ? and password = ?');
            let row = await smt.get(user, pass);
            resolve(row !== undefined ? row.username == 'admin' : false);
        } catch(e) {
            reject(e);
        }
    });
}
```

This means there is a check for administrator privileges somewhere which implies there is a difference in the user accessing the website (i.e. anonymous users, authenticated users, administrators). Lets also keep this in mind in case we are attempting to exploit some auth bypass.

### WeatherHelper.js

```js
module.exports = {
    async getWeather(res, endpoint, city, country) {

        // *.openweathermap.org is out of scope
        let apiKey = '10a62430af617a949055a46fa6dec32f';
        let weatherData = await HttpHelper.HttpGet(`http://${endpoint}/data/2.5/weather?q=${city},${country}&units=metric&appid=${apiKey}`); 
        
        if (weatherData.name) {
            let weatherDescription = weatherData.weather[0].description;
            let weatherIcon = weatherData.weather[0].icon.slice(0, -1);
            let weatherTemp = weatherData.main.temp;

            switch (parseInt(weatherIcon)) {
                case 2: case 3: case 4:
                    weatherIcon = 'icon-clouds';
                    break;
                case 9: case 10:
                    weatherIcon = 'icon-rain';
                    break;
                case 11:
                    weatherIcon = 'icon-storm';
                    break;
                case 13:
                    weatherIcon = 'icon-snow';
                    break;
                default:
                    weatherIcon = 'icon-sun';
                    break;
            }

            return res.send({
                desc: weatherDescription,
                icon: weatherIcon,
                temp: weatherTemp,
            });
        } 

        return res.send({
            error: `Could not find ${city} or ${country}`
        });
    }
}
```

This one took me a minute to put together. Assuming we control the `endpoint` variable, we may be able to perform some sort of SSRF albeit difficult.

### routes/index.js

If the previous two observations were gold, then this file is the silver. Unsurprisingly, Express makes finding entry points easy. This file contains all the front-end endpoints to the application.

The following `/api/whether` endpoint is most likely the endpoint for getting weather information.

```js
router.post('/api/weather', (req, res) => {
	let { endpoint, city, country } = req.body;

	if (endpoint && city && country) {
		return WeatherHelper.getWeather(res, endpoint, city, country);
	}

	return res.send(response('Missing parameters'));
});	
```

The following three endpoints confirm my thoughts about there being seperation of users:

```js
router.get('/register', (req, res) => {
	return res.sendFile(path.resolve('views/register.html'));
});

router.post('/register', (req, res) => {

	if (req.socket.remoteAddress.replace(/^.*:/, '') != '127.0.0.1') {
		return res.status(401).end();
	}

	let { username, password } = req.body;

	if (username && password) {
		return db.register(username, password)
			.then(()  => res.send(response('Successfully registered')))
			.catch(() => res.send(response('Something went wrong')));
	}

	return res.send(response('Missing parameters'));
});

router.get('/login', (req, res) => {
	return res.sendFile(path.resolve('views/login.html'));
});

router.post('/login', (req, res) => {
	let { username, password } = req.body;

	if (username && password) {
		return db.isAdmin(username, password)
			.then(admin => {
				if (admin) return res.send(fs.readFileSync('/app/flag').toString());
				return res.send(response('You are not admin'));
			})
			.catch(() => res.send(response('Something went wrong')));
	}
	
	return re.send(response('Missing parameters'));
});
```

## The Spice

Since the SQLi looks the most promising, lets dig into that first:

```js
router.post('/register', (req, res) => {

	if (req.socket.remoteAddress.replace(/^.*:/, '') != '127.0.0.1') {
		return res.status(401).end();
	}

	let { username, password } = req.body;

	if (username && password) {
		return db.register(username, password)
			.then(()  => res.send(response('Successfully registered')))
			.catch(() => res.send(response('Something went wrong')));
	}

	return res.send(response('Missing parameters'));
});
```

Looking at this code however, I notice a glaring issue: The application only permits localhost to reach this endpoint. I try a few different things to bypass the this input validation (CRLF break, NULL) but don't have any luck. Let's put this on the back-burner.

My other interesting observation was the potential SSRF. The endpoint to access the business code is:

```js
router.post('/api/weather', (req, res) => {
	let { endpoint, city, country } = req.body;

	if (endpoint && city && country) {
		return WeatherHelper.getWeather(res, endpoint, city, country);
	}

	return res.send(response('Missing parameters'));
});	
```

I also capture a request to this endpoint:

```
POST /api/weather HTTP/1.1
Host: 157.245.43.189:32216
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://157.245.43.189:32216/
Content-Type: application/json
Content-Length: 68
Origin: http://157.245.43.189:32216
Connection: close

{"endpoint":"api.openweathermap.org","city":"Laurel","country":"US"}
```

Looks like we control the endpoint, city, and country. This is great however lets take a look at the URL for the request again:

```
http://${endpoint}/data/2.5/weather?q=${city},${country}&units=metric&appid=${apiKey}
```

There doesn't appear to be a lot we can do given the restrictions. I'll admit, I was a bit stumped on this for a while.

- http response splitting (https://owasp.org/www-community/attacks/HTTP_Response_Splitting)
- http request smuggling (https://portswigger.net/web-security/request-smuggling)