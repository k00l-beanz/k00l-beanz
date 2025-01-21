#!/bin/bash

export AFL_USE_ASAN=1
afl-clang-lto -fsanitize=address fuzz-buf.c -o fuzz \
	-I../libexif-0_6_14-release/ ../libexif-0_6_14-release/libexif/.libs/libexif.a -lm
