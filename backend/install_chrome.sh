#!/bin/bash

# Update package lists
apt-get update

# Install necessary dependencies
apt-get install -y wget gnupg2

# Add Google Chrome's GPG key
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -

# Add the Google Chrome repository
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

# Update package lists again
apt-get update

# Install Google Chrome
apt-get install -y google-chrome-stable
