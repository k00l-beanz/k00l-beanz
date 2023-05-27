#!/bin/bash

cd Logs

while read -r line; do
	newFile=$(echo "$line" | rev | cut -d '.' -f 2- | rev)
	evtx_dump.py "$line" > ../dump/"$newFile".dump
done < ../files.txt
