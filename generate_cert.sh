#!/bin/bash

# Clear screen for a clean setup look
clear

echo -e "\033[96m[*] Checking dependencies for TrackMeNow Secure Layer...\033[0m"

# If running inside Termux, make sure openssl is installed automatically
if [ -d "/data/data/com.termux" ]; then
    echo -e "\033[93m[!] Termux environment detected. Ensuring OpenSSL is installed...\033[0m"
    pkg install openssl -y -q
fi

echo -e "\033[96m[*] Compiling self-signed SSL/TLS certificates...\033[0m"

# Generate the actual keys required by Flask
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 -subj "/CN=localhost" 2>/dev/null

if [ -f "cert.pem" ] && [ -f "key.pem" ]; then
    echo -e "\033[92m[+] SUCCESS: Cryptographic credentials generated natively!\033[0m"
    echo -e "\033[92m[+] Files deployed: cert.pem, key.pem\033[0m"
else
    echo -e "\033[91m[-] CRITICAL ERROR: Failed to compile credentials. Please check OpenSSL permissions.\033[0m"
fi