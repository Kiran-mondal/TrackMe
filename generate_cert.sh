#!/bin/bash

# Clear terminal screen for a professional setup layout
clear

echo -e "\033[96m[*] Checking environment and dependencies for TrackMeNow Secure Layer...\033[0m"

# Auto-detect Termux environment and ensure OpenSSL is active
if [ -d "/data/data/com.termux" ]; then
    echo -e "\033[93m[!] Termux environment detected. Synchronizing OpenSSL binaries...\033[0m"
    pkg install openssl -y -q
fi

echo -e "\033[96m[*] Compiling self-signed SSL/TLS cryptographic certificates...\033[0m"

# Explicitly create files first to force file system permissions
touch cert.pem key.pem

# Compile credentials while bypassing standard configuration blocks using internal echo config
openssl req -x509 -newkey rsa:4096 -nodes \
    -out cert.pem \
    -keyout key.pem \
    -days 365 \
    -subj "/CN=localhost" \
    -config <(echo -e "[req]\ndistinguished_name=req_distinguished_name\n[req_distinguished_name]")

# Validation block to confirm file creation
if [ -s "cert.pem" ] && [ -s "key.pem" ]; then
    echo -e "\033[92m[+] SUCCESS: Cryptographic credentials generated natively!\033[0m"
    echo -e "\033[92m[+] Files deployed: cert.pem, key.pem\033[0m"
else
    echo -e "\033[91m[-] CRITICAL ERROR: Failed to compile credentials. Please check storage permissions.\033[0m"
fi
