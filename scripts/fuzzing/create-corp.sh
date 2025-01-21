#!/bin/bash

test "$1" = "-h" -o -z "$1" -o -z "$2" && {
        echo "usage: $0 in/ \"exec cmd --foo @@\""
        exit 1
}

test -d "$1" || { echo "[!] Error: not a directory: $1"; exit 1; }

rm -drf uin rin 2>/dev/null
mkdir uin rin 2>/dev/null

afl-cmin -i "$1" -o "uin" -- "$2" || { echo "[!] Error: afl-cmin failed"; exit 1; }
