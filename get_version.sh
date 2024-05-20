#!/bin/bash

output=$(google-chrome --version)

version=$(echo "$output" | awk '{print $3}')

echo "Version is: $version"