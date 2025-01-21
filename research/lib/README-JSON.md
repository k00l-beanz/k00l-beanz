# Fuzzing Lib - JSON

## Information Gathering

- [vurtun/lib](https://github.com/vurtun/lib)

## Identify Entry Point

- json_load
- json_num
- json_parse

- When using [libfuzzer](https://llvm.org/docs/LibFuzzer.html), you might need to pass `-` to the input to let AFL++ know to read from stdin. This is mentioned [here](https://github.com/AFLplusplus/AFLplusplus/blob/stable/utils/aflpp_driver/README.md).

## Compile w/o Instrumentation
- I'll first write the harness. This can be found in json-harness.cc.
- Building json harness. I'll copy over any necessary header files to make things easier
- I'll also be using libfuzzer since it's fast as.... 
```bash
cp ../json.h ./json.h
clang++ -fsanitize=fuzzer ./json-harness.cc -o ./json-harness
```

## Compile w/ Instrumentation

- I'll compile with various sanitizers

- Building json harness using ASAN
```bash
AFL_USE_ASAN=1 afl-clang-lto++ ./json-harness.cc -o ./json-harness -fsanitize=fuzzer,address
```

## Build Corpus

- I'll use the [go-fuzz-corpus - json](https://github.com/dvyukov/go-fuzz-corpus) as my initial corpus

- Reduce corpus which do not provide new coverage and minimize the corpus files
```bash
mkdir rin uin && \
    afl-cmin -i in/ -o uin/ -- ./json-harness - && \
    cd uin && for i in *; do afl-tmin -i "$i" -o "../rin/$i" -- ../json-harness -; done && \
    cd ../ && rm -drf in uin && mv rin in
```

## Fuzz the Target

- Start fuzzing
```bash
afl-fuzz -i in/ -o out/ -t 20000 -x /AFLplusplus/dictionaries/json.dict -a text -- ./json-harness
```

## Checking Performance

```bash
$ afl-stat.sh asan-out/default/
File: /root/research/lib/fuzz/json/asan-out/default
execs_done        : 4241878
execs_per_sec     : 54466.85
run_clock         : 0:00:01:17
run_time          : 77
stability         : 100.00%
```

## Checking Coverage

**Compile with Coverage**

```bash
g++ --coverage ./cov.cc -o ./cov && \
    lcov --zerocounters --directory ./ && \
    lcov --capture --initial --directory ./ --output-file app.info
```

- After feeding all the test cases in the AFL++ queue:
```bash
$ genhtml --highlight --legend -output-directory ./html-coverage/ ./app.info
Reading data file ./app.info
Found 2 entries.
Found common filename prefix "/root/research/lib/fuzz"
Writing .css and .png files.
Generating output.
Processing file json/json.h
Processing file json/cov.cc
Writing directory view page.
Overall coverage rate:
  lines......: 34.1% (155 of 454 lines)
  functions..: 23.1% (6 of 26 functions)
```
