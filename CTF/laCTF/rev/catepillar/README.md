# Caterpillar
JavaScript obfuscation is always fun. Some interesting observations from playing around with parts of `catepillar.js`:

```javascript
const flag = "lactf{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}";
flag.charCodeAt(-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~[]);
```

This returns the character code `88` which is `X`. I'd like to know which `X` it is refering to so I create a flag where every character is unique.

```javascript
var flag = "lactf{ABCDEFGHIJKLMNOPQRSTUVWXYZbdeghijkmnopqrsuv0123456789}";
flag.charCodeAt(-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~[]);
```

This returns the character code `76` which is `L` which is the 18th element of the `flag` string. I then check what `-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~[]` evaluates to.

```javascript
console.log(-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~[]);
````

This comes out as `108` or `l`. Rather than going through each individual conditional clause, I decide to automate the process. This is my approach:

1. Identify the index that will be replaced
2. Determine the new character to insert at that index
3. Replace the old character with the new one.

I first grab all the `flag.charCodeAt(...)`. In order to do this I change the format of the `caterpillar.js` file so that every `flag.charCodeAt(...)` and `-~-~...` is on its own line. I then regex and put everything into a list.

```bash
cat caterpillar.js | grep "^flag.charCodeAt\(.*\)" | sed -e "s/\n/,/g"
```

Copy this into a new JavaScript file and place it into an array. Then do the same for what characters we want:

```bash
cat caterpillar.js | grep "^==" | cut -d ' ' -f 2 | sed -z "s/\n/,/g"
```

It doesn't really matter how you do this as long as you're able to get everything inserted into an array in a new JS file. Then convert every character from the original flag into it's index. You can't operate directly on the same flag due to the possibility of creating two or more characters in the same flag. Thus, we must operate on an original flag which only has unique characters. Once you have the index, take the new characters and insert them accordingly. The main loop will be:

```javascript
var flag = [];
for (var i = 0; i < flagIndexes.length; i++) {
	var charCode = flagIndexes[i];
	var char = String.fromCharCode(charCode);
	var index = originalFlag.indexOf(char);
	var newChar = String.fromCharCode(newCharacters[i]);
	flag[index] = newChar;
}
```

You can probably due this more elegantly but I'm not proficient in JS.

Flag: `lactf{th3_hungry_l1ttl3_c4t3rp1ll4r_at3_th3_fl4g_4g41n}`