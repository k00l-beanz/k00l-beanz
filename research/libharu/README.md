# libharu

## Information Gathering

- [libharu github](https://github.com/libharu/libharu)
- I'll fuzz [v2.4.4](https://github.com/libharu/libharu/archive/refs/tags/v2.4.4.tar.gz)

## Instrumenting Application

**Building without instrumentation**
- This will dump 'compile_commands.json'. Load this into Understand
```bash
mkdir build && \
    cd build && \
    cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .. && \
    make
```

**Building with instrumentation**
```bash
export AFL_USE_ASAN=1
mkdir build && \
    cd build && \
    cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_C_COMPILER=afl-clang-lto -DCMAKE_CXX_COMPILER=afl-clang-lto++ .. && \
    make
```

**Compiling Harness**

- There are a bunch of entry points in this project
    - `HPDF_LoadRawImageFromMem`

```bash
AFL_USE_ASAN=1 afl-clang-lto++ -fsanitize=address,fuzzer ./fuzz.cc -o fuzz ./libhpdf.a -I../libharu-2.4.4/include/ -I ../libharu-2.4.4/build/include/
```

## Preparing Fuzzing Campaign

- Remove inputs which result in similar coverage
```bash
afl-cmin -i in -o uin -- ./fuzz -
```

- Reduce the size of the inputs
```bash
mkdir rin && cd uin
for f in *; do afl-tmin -i "$f" -o "../rin/$f" -- ../fuzz -; done
```

## Fuzzing the target

- Single afl node
```bash
afl-fuzz -i in/ -o out/ -t 20000 -a binary -x /AFLplusplus/dictionaries/pdf.dict -- ./fuzz -
```

- Multiple afl nodes
```bash
afl-fuzz -M master -i in/ -o out/ -t 20000 -a binary -x /AFLplusplus/dictionaries/pdf.dict -- ./fuzz -
for i in $(seq 1 3); do afl-fuzz -S "slave$i" -i in/ -o out/ -t 20000 -a binary -x /AFLplusplus/dictionaries/pdf.dict -- ./fuzz - > /dev/null 2>&1 &; done
```