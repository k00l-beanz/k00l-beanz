#!/bin/bash

afl-whatsup -s out > res/whatsup.txt
afl-plot out/default res
