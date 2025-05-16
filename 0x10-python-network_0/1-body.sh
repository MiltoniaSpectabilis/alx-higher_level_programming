#!/bin/bash
# This script takes in a url, sends a GET request and displays its status code response
curl -si "$1" | head -1
