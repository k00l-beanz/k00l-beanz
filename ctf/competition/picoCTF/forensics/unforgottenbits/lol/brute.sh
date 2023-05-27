while read -r line; do
    steghide extract -sf 7.bmp --passphrase "$line" 2> /dev/null

    if [ "$?" -eq 0 ]; then
        echo "$line" 
        break
    fi

done < passwords