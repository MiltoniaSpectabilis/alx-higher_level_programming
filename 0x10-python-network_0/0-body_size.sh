#!/bin/bash
# Takes in a url and displays the size of the response body
curl -s "$1" | wc -c
