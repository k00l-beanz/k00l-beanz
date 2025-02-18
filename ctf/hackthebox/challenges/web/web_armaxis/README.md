# Armaxis

## Information Gathering

In the dockerfile, the following is downloaded
    - [MailHog binary v1.0.1](https://github.com/mailhog/MailHog/releases/download/v1.0.1/MailHog_linux_amd64)


## VR Notes

- Potential OS command injection in `challenge/challenge/markdown.js`
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