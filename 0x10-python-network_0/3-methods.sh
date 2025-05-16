#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept
curl -sIX OPTIONS "$1" | grep methods | cut -f2- -d' '
