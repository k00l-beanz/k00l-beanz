# Level 05

## Information Gathering

- [CVE-2017-9048](https://nvd.nist.gov/vuln/detail/CVE-2017-9048)
```
libxml2 20904-GITv2.9.4-16-g0741801 is vulnerable to a stack-based buffer overflow. The function xmlSnprintfElementContent in valid.c is supposed to recursively dump the element content definition into a char buffer 'buf' of size 'size'. At the end of the routine, the function may strcat two more characters without checking whether the current strlen(buf) + 2 < size. This vulnerability causes programs that use libxml2, such as PHP, to crash.
```

- [LibXML2 Repository](https://gitlab.gnome.org/GNOME/libxml2)
- [libxml2 v2.9.4](https://gitlab.gnome.org/GNOME/libxml2/-/archive/v2.9.4/libxml2-v2.9.4.tar.gz)
- [libxml documentation](https://gitlab.gnome.org/GNOME/libxml2/-/wikis/home)
- [xmllint documentation](https://www.mankier.com/1/xmllint)

## Instrumenting the target

**Compile without instrumentation**
```bash
autoreconf -ivf && \
    ./configure --disable-shared && \
    make
```

**Compile with instrumentation**
- I'll be using ASAN as my sanitizer
```bash
export AFL_USE_ASAN=1
autoreconf -ivf && \
    CC=afl-clang-lto CXX=afl-clang-lto++ CFLAGS="-fsanitize=address" CXXFLAGS="-fsanitize=address" ./configure --disable-shared && \
    make
```

**Compiling Harness**
```bash
AFL_USE_ASAN=1 afl-clang-lto++ -fsanitize=address,fuzzer -I../libxml2-2.9.4/include ./fuzz.cc -o ./fuzz ../libxml2-2.9.4/.libs/libxml2.a -lz -lpthread -lm
```

## Preparing the fuzzing campaign

**Selecting an Entry Point**
- `xmllint` is a good entry point.
- Writing my own harness
    - `xmlReadMemory`


**Collecting input**
- I'll be using the [go-fuzz-corpus](https://github.com/dvyukov/go-fuzz-corpus) xml corpus for this campaign

**Minimizing all corpus files**
- Removing corpus which provide the same coverage
```bash
afl-cmin -i in -o uin -- ./fuzz -
```

- Minimizing corpus size
```bash
mkdir rin
for i in *; do afl-tmin -i "$i" -o "../rin/$i" -- ../fuzz -; done
```

## Fuzzing the Target

```bash
afl-fuzz -i in/ -o out/ -t 20000 -a text -x /AFLplusplus/dictionaries/xml.dict -- ./xmllint @@
afl-fuzz -i in/ -o out/ -t 20000 -a text -x /AFLplusplus/dictionaries/xml.dict -- ./fuzz
```