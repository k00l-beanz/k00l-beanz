#!/bin/bash

test "$1" = "-h" -o -z "$1" && {
        echo "usage $0 out \"exec cmd -foo @@\""
        exit 1
}

test -d "$1" || { echo "[!] Error: Not a directory: $1"; exit 1; }

# cleanup
rm -drf html-coverage *.gcna *.gcno app*

g++ --coverage ./cov.cc -o ./cov || { echo "[!] Error: Failed to compile with coverage"; exit 1; }
lcov --zerocounters --directory ./ || { echo "[!] Error: Failed to reset counters"; exit 1; }
lcov --capture --initial --directory ./ --output-file app.info || { echo "[!] Error: Failed to run baseline coverage data"; exit 1; }

QUEUE=`realpath "$1"`
for f in $(ls "$1"); do
        fullpath="$QUEUE/$f"
        echo "[*] Running $fullpath"
        cat "$fullpath" | ./cov
        lcov --no-checksum --directory ./ --capture --output-file ./app.info
done

genhtml --highlight --legend -output-directory ./html-coverage/ ./app.info

exit 0