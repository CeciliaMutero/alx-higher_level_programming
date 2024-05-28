#!/bin/bash
# takes a URL as input,sends a GET request,if the status code is 200
# displays the body of the response
if [ "$(curl -sL -w "%{http_code}" "$1" -o response.txt)" -eq 200 ]; then cat response.txt; fi
