# Level 05

## Information Gathering

- [CVE-2017-9048](https://nvd.nist.gov/vuln/detail/CVE-2017-9048)
```
libxml2 20904-GITv2.9.4-16-g0741801 is vulnerable to a stack-based buffer overflow. The function xmlSnprintfElementContent in valid.c is supposed to recursively dump the element content definition into a char buffer 'buf' of size 'size'. At the end of the routine, the function may strcat two more characters without checking whether the current strlen(buf) + 2 < size. This vulnerability causes programs that use libxml2, such as PHP, to crash.
```

- [LibXML2 Repository](https://gitlab.gnome.org/GNOME/libxml2)
- [libxml2 v2.9.4](https://gitlab.gnome.org/GNOME/libxml2/-/archive/v2.9.4/libxml2-v2.9.4.tar.gz)
- [libxml documentation](https://gitlab.gnome.org/GNOME/libxml2/-/wikis/home)
