#!/bin/bash

export AFL_USE_ASAN=1

CC=afl-clang-lto CXX=afl-clang-lto++ CFLAGS="-fsanitize=address" CXXFLAGS="-fsanitize=address" \
	./configure --enable-shared=no && \
        make
