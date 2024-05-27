#!/bin/bash
if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

URL=$1

BODY_SIZE=$(curl -s "$URL" | wc -c)

echo "$BODY_SIZE"
