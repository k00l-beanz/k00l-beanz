# Level 4

## Objectives

- How to measure code coverage using LCOV
- How to use code coverage data to improve the effectiveness of fuzzing

## Information Gathering

- [libtiff 4.0.6](https://gitlab.com/libtiff/libtiff/-/archive/v4.0.6/libtiff-v4.0.6.tar.gz)
- [libtiff api](http://libtiff.gitlab.io/libtiff/)

- [CVE-2016-9297](https://www.cvedetails.com/cve/CVE-2016-9297/)
```
The TIFFFetchNormalTag function in LibTiff 4.0.6 allows remote attackers to cause a denial of service (out-of-bounds read) via crafted TIFF_SETGET_C16ASCII or TIFF_SETGET_C32_ASCII tag values.
```

## Compile w/o Instrumentation

- Compile
```bash
./configure --enable-shared=no && make
```

## Compile w/ Instrumentation

```bash
export AFL_USE_ASAN=1
CC=afl-clang-lto CXX=afl-clang-lto++ CFLAGS="-fsanitize=address" CXXFLAGS="-fsanitize=address" ./configure --enable-shared=no && make
cd tools && make
```

## Select an Entry Point

- There are a bunch of tools we can use to reach our target function, I'll be using `libtiff-v4.0.6/tools/tiff2pdf.c`
- Other options are
    - `libtiff-v4.0.6/tools/raw2tiff.c`
    - `libtiff-v4.0.6/tools/tiff2ps.c`
    - `libtiff-v4.0.6/tools/tiffdump.c`
- There's also the API

## Creating Corpus

- [go-fuzz corpus - tiff](https://github.com/dvyukov/go-fuzz-corpus/tree/master/tiff/corpus)

- Reduce corpus which do not provide new coverage
```bash
afl-cmin -i in/ -o uin -- ./tiff2pdf @@
```

- Minimize corpus files
```bash
cd uin
for i in *; afl-tmin -i "$i" -o "../rin/$i" -- ../tiff2pdf @@; done
```

## Fuzz the Target

- Start fuzzing
```bash
afl-fuzz -i in/ -o out/ -t 20000 -m 1000 -- ./tiff2pdf @@
```

## Checking Performance

- While running
```bash
afl-whatsup -s out/
```

- Graphical stats
```bash
afl-plot out/default /srv
```

- Quick post-fuzz stats
```bash
afl-stat.sh out-0/default/
```

## Coverage

- [vanhauser-thc/afl-cov](https://github.com/vanhauser-thc/afl-cov)

- Compile with coverage
```bash
./configure --enable-shared=no CFLAGS="-fprofile-arcs -ftest-coverage" CXXFLAGS="-fprofile-arcs -ftest-coverage" && make; cd tools && make && cd ..
afl-cov -d ../fuzz/out/ --coverage-cmd "tools/tiff2pdf @@" --code-dir .

# To track coverage during a campaign
afl-cov -d ../fuzz/out/ --live --coverage-cmd "tools/tiffpdf @@" --code-dir .
# Then open a seperate terminal and start afl-fuzz
```

- After your coverage has been recorded, you might need to manually generate the html report
```bash
genhtml --highlight --legend --ignore-errors source --output-directory ./html-coverage
```

- quick and dirty coverage
```bash
afl-showmap -C -i out/ -o /dev/null -- ./tiff2pdf @@
```