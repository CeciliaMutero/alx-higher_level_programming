#!/bin/bash
# script that takes a URL as input, sends a request,displays the size
curl - sI "$1" | grep - i Content-Length | awk '{print $2}9'
