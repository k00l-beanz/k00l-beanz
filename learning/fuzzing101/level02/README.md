# Exercise 2

## Information Gathering

- [Link to libexif 0.6.14 tarball](https://github.com/libexif/libexif/archive/refs/tags/libexif-0_6_14-release.tar.gz)
- [Link to exif 0.6.15 tarball](https://github.com/libexif/exif/archive/refs/tags/exif-0_6_15-release.tar.gz)

[CVE-2009-3895](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-3895)
```
Heap-based buffer overflow in the exif_entry_fix function (aka the tag fixup routine) in libexif/exif-entry.c in libexif 0.6.18 allows remote attackers to cause a denial of service or possibly execute arbitrary code via an invalid EXIF image. NOTE: some of these details are obtained from third party information. 
```

[CVE-2012-2836](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-2836)
```
The exif_data_load_data function in exif-data.c in the EXIF Tag Parsing Library (aka libexif) before 0.6.21 allows remote attackers to cause a denial of service (out-of-bounds read) or possibly obtain sensitive information from process memory via crafted EXIF tags in an image. 
```

## Building w/o Instrumentation

- Install dependenices
```sh
sudo apt install libtool gettext -y
```

- Build
```sh
autoreconf -ivf && ./configure --enable-shared=no && make
```

## Selecting an Entry Point

- I know that I want to target the vulnerable exif_entry_fix function from CVE-2009-3895
- Walking up the CFG from this function leads me to two entry points:
1. `libexif-0_6_14-release/libexif/exif-entry.c` - exif_data_new_from_data
2. `libexif-0_6_14-release/libexif/exif-entry.c` - exif_data_new_from_file

- All functions in `libexif-0_6_14-release/libexif/exif-entry.c` seem like promising entry points.
- I'll implement both, but lets go with the `exif_data_new_from_file` first to see the difference in performance later on.
- Lets check the [documentation](https://libexif.github.io/api/index.html) and see if there are any examples of this function being used.

## Instrument Library

- Instrument the library for coverage and add ASAN
```bash
export AFL_USE_ASAN=1
CC=afl-clang-lto CXX=afl-clang-lto++ CFLAGS="-fsanitize=address" CXXFLAGS="-fsanitize=address" ./configure --enable-shared=no && make
```

## Write and Compile the Target

- I found this [example](https://github.com/libexif/libexif/blob/master/contrib/examples/photographer.c) using the `exif_data_new_from_file` subroutine. Doesn't appear to be any setup or library initialization.
- Compile the harness:
```bash
export AFL_USE_ASAN=1
afl-clang-lto -fsanitize=address fuzz.c -o fuzz -I../libexif-0_6_14-release/ ../libexif-0_6_14-release/libexif/.libs/libexif.a -lm
```

## Collecting and Minimizing Inputs

- [ianare/exif-samples](https://github.com/ianare/exif-samples)
- [getlantern/exif-image-corpus](https://github.com/getlantern/exif-image-corpus)

```bash
afl-cmin -i in/ -o uin/ -- ./fuzz @@
```

**Optional: Minimize corpus files**

```bash
#!/bin/bash

mkdir input
cd INPUTS_UNIQUE
for i in *; do
  afl-tmin -i "$i" -o "../input/$i" -- bin/target -someopt @@
done
```

## Fuzzing the Target

- Configure your system for afl-fuzz
```bash
afl-system-config
afl-fuzz -i in/ -o out/ -t 20000 -- ./fuzz @@
```

## Checking Performance

- Check current status of AFL++
```bash
afl-whatsup -s ./out/
```

- Plot the performance
```bash
mkdir srv && afl-plot out/default/ srv/
cd src/ && python3 -m http.server
```

- Check coverage
```bash
afl-showmap -C -i out/ -o /dev/null -- ./fuzz @@
[*] Reading from directory 'out/'...
[*] Scanning 'out/'...
[*] Scanning 'out//default'...
[*] Scanning 'out//default/crashes'...
[*] Scanning 'out//default/hangs'...
[*] Scanning 'out//default/queue'...
[+] Captured 770 tuples (map size 6553, highest value 255, total values 55834) in '/dev/null'.
[+] A coverage of 770 edges were achieved out of 6592 existing (11.68%) with 450 input files.
```

## References

- [AFL (american fuzzy lop)](https://afl-1.readthedocs.io/en/latest/)
- [fuzzing_in_depth](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md)
- [Harness training](https://github.com/mykter/afl-training/blob/main/harness/README.md)
- [A Look at AFL++ Under The Hood](https://blog.ritsec.club/posts/afl-under-hood/)
- [The afl-fuzz approach](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/afl-fuzz_approach.md)
- [best_practices](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/best_practices.md)
- [fuzzah/exeptor](https://github.com/fuzzah/exeptor)
- [vanhauser-thc/afl-cov](https://github.com/vanhauser-thc/afl-cov)