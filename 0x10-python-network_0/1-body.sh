#!/bin/bash
# This script takes in a url, sends a GET request and displays its status code response
curl -sI "$1" | head -1
