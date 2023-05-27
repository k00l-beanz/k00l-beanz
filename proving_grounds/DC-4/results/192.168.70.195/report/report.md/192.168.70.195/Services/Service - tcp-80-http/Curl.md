```bash
curl -sSik http://192.168.70.195:80/
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp80/tcp_80_http_curl.html](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp80/tcp_80_http_curl.html):

```
HTTP/1.1 200 OK
Server: nginx/1.15.10
Date: Fri, 02 Dec 2022 02:43:49 GMT
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

<!DOCTYPE html>
<html>
<head>
<title>System Tools</title>
<link rel="stylesheet" href="css/styles.css">
</head>

<body>
	<div class="container">
		<div class="inner">
			<h2>Admin Information Systems Login</h2>
			<form action="login.php" method="post">
				Username:<br>
				<input type="text" name="username" value=""><p>
				Password:<br>
				<input type="password" name="password" value=""><p>
				<input type="submit" value="Submit">
			</form>

		</div>
	</div>
</body>
</html>


```
