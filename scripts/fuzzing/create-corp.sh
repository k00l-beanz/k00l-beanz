#!/bin/bash

# Handle args
test "$1" = "-h" -o -z "$1" -o -z "$2" && {
        echo "usage: $0 [-c] in/ \"exec cmd --foo @@\""
        exit 1
}

test "$1" = "-c" && { OPT1="true"; shift; }
test -d "$1" || { echo "[!] Error: not a directory: $1"; exit 1; }

# Prepare working directory
rm -drf uin rin
mkdir uin rin

afl-cmin -i "$1" -o "uin" -- "$2" || { echo "[!] Error: afl-cmin failed"; exit 1; }
IN=`realpath "$1"`
for f in $(ls "$1"); do
        fullpath="$IN/$f"
        afl-tmin -i "$fullpath" -o "rin/$f" -- "$2" || { echo "[!] Error: afl-tmin failed"; exit 1; }
done

# Optional cleanup
test -n "$OPT1" && { rm -drf "in" "uin"; mv rin "in"; }

exit 0